from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int

class CourseResponse(CourseCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

class DepartmentCreate(BaseModel):
    name: str
    head_of_dept: str
    budget: float

class DepartmentResponse(DepartmentCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)