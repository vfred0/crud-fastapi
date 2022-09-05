import uuid
from pydantic import BaseModel
from typing import List, Optional


class Student(BaseModel):
    id: Optional[int]
    name: str
    age: int
