from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from contextlib import asynccontextmanager

from database import engine, Base, get_db
import models
import schemas

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title='Course Management API',
    lifespan=lifespan
)

@app.post('/api/departments/', response_model=schemas.DepartmentResponse, status_code=status.HTTP_201_CREATED)
async def create_department(dept: schemas.DepartmentCreate, db: AsyncSession = Depends(get_db)):
    db_dept = models.Department(name=dept.name, head_of_dept=dept.head_of_dept, budget=dept.budget)
    db.add(db_dept)
    await db.flush()
    return db_dept

@app.post('/api/courses/', response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: schemas.CourseCreate, db: AsyncSession = Depends(get_db)):
    result_dept = await db.execute(select(models.Department).where(models.Department.id == course.department_id))
    if not result_dept.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Department with given ID does not exist")

    result_code = await db.execute(select(models.Course).where(models.Course.code == course.code))
    if result_code.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Course code must be unique")

    db_course = models.Course(name=course.name, code=course.code, credits=course.credits, department_id=course.department_id)
    db.add(db_course)
    await db.flush()
    return db_course

@app.get('/api/courses/', response_model=List[schemas.CourseResponse])
async def get_courses(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    query = select(models.Course).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()