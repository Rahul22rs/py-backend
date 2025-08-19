from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from app.models.base import Base
from app.models.Movie import Movie



def get_engine() -> Engine:
    CONN_STRING = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/localdb"
    return create_engine(CONN_STRING, echo=False)


def get_session(engine: Engine) -> Session:
    session = Session(engine)
    return session


def execute_ddl(engine: Engine):
    Base.metadata.create_all(engine)
