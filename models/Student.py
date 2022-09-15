from typing import List, Optional
import uuid

# from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

from utils.Skill import Skill


class Student(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default=uuid.uuid4(), primary_key=True)
    name: str = Field(max_length=25, nullable=False)
    age: int = Field(default=0, ge=0, le=100, nullable=False)
    #skills: List[Skill] = Relationship(back_populates="id")


