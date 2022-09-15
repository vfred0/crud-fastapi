from typing import List

from fastapi.encoders import jsonable_encoder

from models.Student import Student
from repository.DatabaseRepository import DatabaseRepository

# from sqlalchemy.sql import text


class StudentRepository(DatabaseRepository):
    def __init__(self) -> None:
        super().__init__()

    def save(self, student: Student):
        self._db.add(student)
        self._db.commit()

    def get_students(self) -> List[Student]:
        return self._db.query(Student).all()

    def update(self, student):
        self._db.query(Student).filter(Student.id == student.id).update(
            jsonable_encoder(student)
        )
        self._db.commit()

    def delete(self, id: int):
        self._db.query(Student).filter(Student.id == id).delete()
        self._db.commit()

    def get_students_by_skill(self, skill: str) -> List[Student]:
        return self._db.query(Student).filter(Student.skills.contains(skill)).all()
