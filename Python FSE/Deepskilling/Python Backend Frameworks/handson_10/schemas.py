from pydantic import BaseModel, ConfigDict
from typing import List

class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    model_config = ConfigDict(from_attributes=True)

class DepartmentCreate(BaseModel):
    name: str
    head_of_dept: str

class DepartmentResponse(BaseModel):
    id: int
    name: str
    head_of_dept: str
    courses: List[CourseResponse] = [] # Nested relationship payload
    model_config = ConfigDict(from_attributes=True)