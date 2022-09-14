from enum import Enum


class Skill(Enum):
    JAVA = "Java"
    PYTHON = "Python"
    TYPESCRIPT = "TypeScript"
    CSHARP = "C#"
    POSTGRESQL = "PostgreSQL"
    MYSQL = "MySQL"

    def __init__(self, value) -> None:
        self._value_ = value

    @staticmethod
    def all() -> list:
        return [i for i in Skill]

    @staticmethod
    def get(position: int):
        return Skill.all()[position]
