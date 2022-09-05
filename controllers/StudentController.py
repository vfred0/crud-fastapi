import json
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from models.Student import Student


class StudentController:
    router = APIRouter(
        prefix="/api/students",
        # tags=["students"],
        responses={404: {"message": "No encontrado"}},
    )

    @router.get("/", response_model=List[Student])
    async def get_students():
        print("MOSTRAR")
        students: List[Student] = [
            Student(id=1, name="Estudiante 1", age=19),
            Student(id=2, name="Estudiante 2", age=20),
            Student(id=3, name="Estudiante 3", age=21),
        ]
        return JSONResponse(status_code=200, content={"result": json.dumps(students.__str__()) })


    @router.post("/save", response_model=str)
    async def save(student: Student):
        students: List[Student] = [
            Student(name="Estudiante 1", age=19),
            Student(name="Estudiante 2", age=20),
            Student(name="Estudiante 3", age=21),
        ]
        students.append(student)
        return f"Student => {students}"

    @router.delete("/delete/{id}", response_model=str)
    async def delete(id: int):
        students: List[Student] = [
            Student(id=1, name="Estudiante 1", age=19),
            Student(id=2, name="Estudiante 2", age=20),
            Student(id=3, name="Estudiante 3", age=21),
        ]

        # index = 0
        # for student in students:
        #     if student.id == id:
        #         print(f"{student.id} == {id} => {index} {students[index]}")
        #         print(f"Se ha eliminado al estudiante {student}")
        #         students.remove(students[index])
        #     index = index + 1
        students = list(
            filter(
                lambda student: print(f"2Se ha eliminado al estudiante {student}")
                if student.id == id
                else student.id != id,
                students,
            )
        )

        return f"Student => {students}"

    @router.put("/update", response_model=str)
    async def update(student: Student):
        students: List[Student] = [
            Student(id=1, name="Estudiante 1", age=19),
            Student(id=2, name="Estudiante 2", age=20),
            Student(id=3, name="Estudiante 3", age=21),
        ]
        updateStudent: Student = list(
            filter(lambda searchStudent: searchStudent.id == student.id, students)
        )[0]
        print(f"Update => {updateStudent}")
        students[students.index(updateStudent)] = student

        return JSONResponse(
            {
                "message": {
                    "Actualización": {
                        "datos actuales": updateStudent.json(),
                        "nuevos datos": student.json(),
                    },
                    "Estudiantes": json.dumps(students.__str__()),
                },
            }
        )
