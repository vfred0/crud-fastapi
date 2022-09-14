from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseRepository:
    def __init__(self, uri: str = "") -> None:
        self._db = sessionmaker(bind=create_engine(
            "postgres://oqpbfkxrdeubmz:f92aa73eccb70d345215248d89fb86e9e0aea69d42e457e5a5e99679fd3f1af9@ec2-44-206"
            "-137-96.compute-1.amazonaws.com:5432/d9t72egeluahbd",
            echo=True))
