from environs import Env
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(
        self,
        driver_name: str,
        host: int,
        username: str,
        password: str,
        database: str,
        query: dict,
    ):

        self.driver_name = driver_name
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.query = query
        self.url = f"{self.driver_name}://{self.username}:{self.password}@{self.host}/{self.database}"

    @property
    def get_sessionmaker(self):
        engine = create_engine(self.url)
        return sessionmaker(bind=engine)


def load_database(path: str | None = None) -> Database:
    env = Env()
    env.read_env(path)
    return Database(
        driver_name=env("DRIVER_NAME"),
        host=env("HOST"),
        username=env("USER_NAME"),
        password=env("PASSWORD"),
        database=env("DATABASE"),
        query={},
    )
