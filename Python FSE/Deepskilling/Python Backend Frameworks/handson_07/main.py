from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from contextlib import asynccontextmanager
from sqlalchemy.orm import selectinload

from database import engine, Base, get_db
import models
import schemas

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title='Course Management System API',
    version='2.0',
    description='Advanced FastAPI engine handling structural relations, automated schema rules, and background email queues.',
    lifespan=lifespan
)

# Background simulation task handler
def send_confirmation_email(student_email: str, course_name: str):
    import time
    time.sleep(2)  # Simulates mail gateway latency
    print(f"\n[SYSTEM EMAIL QUEUE] -> Sending confirmation mail out to {student_email} for registering in '{course_name}'...\n")

# --- DEPARTMENTS (Fixed & Combined) ---
@app.post('/api/departments/', response_model=schemas.DepartmentResponse, status_code=status.HTTP_201_CREATED, tags=['Departments'])
async def create_department(dept: schemas.DepartmentCreate, db: AsyncSession = Depends(get_db)):
    db_dept = models.Department(
        name=dept.name,
        head_of_dept=dept.head_of_dept,
        budget=dept.budget
    )
    db.add(db_dept)
    
    # 1. Commit changes permanently to the database
    await db.commit() 
    
    # 2. Safely load the object back with its relationship defined (even if empty)
    # This completely eliminates the need for manual "db_dept.courses = []" hacks
    result = await db.execute(
        select(models.Department)
        .options(selectinload(models.Department.courses))
        .where(models.Department.id == db_dept.id)
    )
    return result.scalar_one()


# --- COURSES (Fixed with Commit) ---
@app.post('/api/courses/', response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED, tags=['Courses'])
async def create_course(course: schemas.CourseCreate, db: AsyncSession = Depends(get_db)):
    res_dept = await db.execute(select(models.Department).where(models.Department.id == course.department_id))
    if not res_dept.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Department with given ID does not exist")
        
    res_code = await db.execute(select(models.Course).where(models.Course.code == course.code))
    if res_code.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Course code must be unique")

    db_course = models.Course(name=course.name, code=course.code, credits=course.credits, department_id=course.department_id)
    db.add(db_course)
    
    await db.commit()  # <-- Make sure to commit here!
    await db.refresh(db_course) # Refresh to get the generated ID safely
    return db_course

@app.get('/api/courses/', response_model=List[schemas.CourseResponse], tags=['Courses'])
async def get_courses(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    query = select(models.Course).offset(skip).limit(limit)
    res = await db.execute(query)
    return res.scalars().all()

@app.get('/api/courses/{id}', response_model=schemas.CourseResponse, tags=['Courses'])
async def get_course(id: int, db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(models.Course).where(models.Course.id == id))
    course = res.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.put('/api/courses/{id}', response_model=schemas.CourseResponse, tags=['Courses'])
async def update_course(id: int, updated: schemas.CourseCreate, db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(models.Course).where(models.Course.id == id))
    course = res.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    course.name = updated.name
    course.code = updated.code
    course.credits = updated.credits
    course.department_id = updated.department_id
    await db.flush()
    return course

@app.delete('/api/courses/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Courses'])
async def delete_course(id: int, db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(models.Course).where(models.Course.id == id))
    course = res.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    await db.delete(course)
    return None

# --- STUDENTS ---
@app.post('/api/students/', response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED, tags=['Students'])
async def create_student(student: schemas.StudentCreate, db: AsyncSession = Depends(get_db)):
    res_email = await db.execute(select(models.Student).where(models.Student.email == student.email))
    if res_email.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Email matching this student entry already exists")
    
    db_student = models.Student(
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
        department_id=student.department_id,
        enrollment_year=student.enrollment_year
    )
    db.add(db_student)
    await db.flush()
    return db_student

# --- ENROLLMENTS WITH BACKGROUND TASKS ---
@app.post('/api/enrollments/', response_model=schemas.EnrollmentResponse, status_code=status.HTTP_201_CREATED, tags=['Enrollments'])
async def create_enrollment(payload: schemas.EnrollmentCreate, bg_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    res_student = await db.execute(select(models.Student).where(models.Student.id == payload.student_id))
    student = res_student.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail="Student identity not found")

    res_course = await db.execute(select(models.Course).where(models.Course.id == payload.course_id))
    course = res_course.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course identity not found")

    db_enrollment = models.Enrollment(student_id=payload.student_id, course_id=payload.course_id)
    db.add(db_enrollment)
    await db.flush()

    bg_tasks.add_task(send_confirmation_email, student.email, course.name)
    return db_enrollment