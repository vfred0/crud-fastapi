from pydantic import BaseModel
from typing import List
from models.Student import Student

class Course(BaseModel):
    name: str
    students: List[Student]
