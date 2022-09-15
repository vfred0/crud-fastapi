from sqlmodel import SQLModel, create_engine, Session


class DatabaseRepository:
    def __init__(self, uri: str = "") -> None:
        self.__engine = create_engine(
            "postgresql://oqpbfkxrdeubmz:f92aa73eccb70d345215248d89fb86e9e0aea69d42e457e5a5e99679fd3f1af9@ec2-44-206"
            "-137-96.compute-1.amazonaws.com:5432/d9t72egeluahbd",
            echo=True,
        )
        SQLModel.metadata.create_all(self.__engine)
        self._db = Session(bind=self.__engine)
