from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.Student import Student
from repository.StudentRepository import StudentRepository


class StudentController:
    router = APIRouter(
        prefix="/api/students",
        # tags=["students"],
        responses={404: {"message": "No encontrado"}},
    )

    @router.get("/", response_model=List[Student])
    async def get_students():
        return StudentRepository().get_students()

    @router.post("/save")
    def save(student: Student):
        StudentRepository().save(student)
        return JSONResponse(status_code=200, content={"message": "Estudiante guardado"})

    @router.delete("/delete/{id}")
    def delete(self, id: int):
        self.__repository.delete(id)
        return JSONResponse(
            status_code=200, content={"message": "Estudiante eliminado"}
        )

    @router.put("/update", response_model=str)
    def update(self, student: Student):
        self.__repository.update(student)
        return JSONResponse(
            status_code=200, content={"message": "Estudiante actualizado"}
        )
