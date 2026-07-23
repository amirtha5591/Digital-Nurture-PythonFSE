from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from contextlib import asynccontextmanager

from database import engine, Base, get_db
import models
import schemas
import auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title='Secure Course Management API', version='3.0', lifespan=lifespan)

# --- AUTH ENDPOINTS ---
@app.post('/api/auth/signup', response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED, tags=['Authentication'])
async def signup(user_data: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User).where(models.User.username == user_data.username))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed = auth.hash_password(user_data.password)
    db_user = models.User(username=user_data.username, hashed_password=hashed)
    db.add(db_user)
    await db.flush()  # Saves to database and populates db_user.id
    
    # 🌟 FIX: Directly return a clean dictionary payload matching UserResponse schema
    return {
        "id": db_user.id,
        "username": db_user.username
    }
@app.post('/api/auth/login', response_model=schemas.Token, tags=['Authentication'])
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User).where(models.User.username == form_data.username))
    user = result.scalar_one_or_none()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# --- UNPROTECTED ROUTE ---
@app.post('/api/departments/', response_model=schemas.DepartmentResponse, status_code=status.HTTP_201_CREATED, tags=['Departments'])
async def create_department(dept: schemas.DepartmentCreate, db: AsyncSession = Depends(get_db)):
    db_dept = models.Department(name=dept.name, head_of_dept=dept.head_of_dept, budget=dept.budget)
    db.add(db_dept)
    await db.flush()
    return {
        "id": db_dept.id,
        "name": db_dept.name,
        "head_of_dept": db_dept.head_of_dept,
        "budget": db_dept.budget
    }

# --- SECURE PROTECTED ROUTES (Requires auth dependency!) ---
@app.post('/api/courses/', response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED, tags=['Courses'])
async def create_course(
    course: schemas.CourseCreate, 
    db: AsyncSession = Depends(get_db), 
    current_user: models.User = Depends(auth.get_current_user) # 🔒 Protected!
):
    res_dept = await db.execute(select(models.Department).where(models.Department.id == course.department_id))
    if not res_dept.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Department context not found")
        
    db_course = models.Course(name=course.name, code=course.code, credits=course.credits, department_id=course.department_id)
    db.add(db_course)
    await db.flush()
    return {
        "id": db_course.id,
        "name": db_course.name,
        "code": db_course.code,
        "credits": db_course.credits,
        "department_id": db_course.department_id
    }

@app.delete('/api/courses/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Courses'])
async def delete_course(
    id: int, 
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user) # 🔒 Protected!
):
    res = await db.execute(select(models.Course).where(models.Course.id == id))
    course = res.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    await db.delete(course)
    return None