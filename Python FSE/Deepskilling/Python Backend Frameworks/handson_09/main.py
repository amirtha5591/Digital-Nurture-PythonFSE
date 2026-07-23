from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, ConfigDict
from typing import List
from contextlib import asynccontextmanager
from database import engine, Base, get_db

# --- ORM Model ---
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    code = Column(String(20), unique=True, nullable=False)

# --- Schemas ---
class CourseCreate(BaseModel):
    name: str
    code: str

class CourseResponse(CourseCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

# --- Lifespan ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="Testing Sandbox", lifespan=lifespan)

# --- Routes ---
@app.post("/api/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.code == course.code))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Course code must be unique")
    
    db_course = Course(name=course.name, code=course.code)
    db.add(db_course)
    await db.flush()
    return {"id": db_course.id, "name": db_course.name, "code": db_course.code}

@app.get("/api/courses/", response_model=List[CourseResponse])
async def get_courses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course))
    return result.scalars().all()