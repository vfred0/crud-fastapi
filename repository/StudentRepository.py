import json
from typing import List
from fastapi.encoders import jsonable_encoder

from models.Student import Student


class StudentRepository:
    def __init__(self) -> None:
        self.__URL_DB = "repository/db.json"
        with open(self.__URL_DB, "r") as f:
            self.__students: List[Student] = json.load(f)

    def save(self, student):
        print(f"DEBUG: {self.__students[-1]}")
        student.id = int(self.__students[-1]["id"]) + 1
        student.name = f"{student.name} #{student.id}"
        self.__students.append(jsonable_encoder(student))
        self.__update_students()

    def get_students(self) -> List[Student]:
        return self.__students

    def update(self, student):
        updateStudent: Student = list(
            filter(
                lambda searchStudent: searchStudent["id"] == student.id, self.__students
            )
        )[0]        
        self.__students[self.__students.index(updateStudent)]["id"] = student.id
        self.__students[self.__students.index(updateStudent)]["name"] = student.name
        self.__students[self.__students.index(updateStudent)]["age"] = student.age

        self.__update_students()

    def delete(self, id):
        deleteStudent: Student = list(
            filter(lambda searchStudent: searchStudent['id'] == id, self.__students)
        )[0]

        self.__students.remove(deleteStudent)
        self.__update_students()

    def __update_students(self):
        with open(self.__URL_DB, "w") as f:
            json.dump(self.__students, f)
