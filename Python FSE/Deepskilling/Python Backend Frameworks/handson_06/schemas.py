from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class CourseBase(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class DepartmentCreate(BaseModel):
    name: str
    head_of_dept: str
    budget: float

class DepartmentResponse(BaseModel):
    id: int
    name: str
    head_of_dept: str
    budget: float
    courses: List[CourseResponse] = []
    model_config = ConfigDict(from_attributes=True)