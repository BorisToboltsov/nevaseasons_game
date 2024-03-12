import os

from dotenv import load_dotenv

load_dotenv()

DATABASE = {
    "drivername": os.getenv("DRIVER_NAME"),
    "host": os.getenv("HOST"),
    "port": None,
    "username": os.getenv("USER_NAME"),
    "password": os.getenv("PASSWORD"),
    "database": os.getenv("DATABASE"),
    "query": {},
}

database_url = f"postgresql+psycopg2://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}/{DATABASE['database']}"
