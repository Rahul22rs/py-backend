from sqlalchemy import create_engine
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from app.models.base import Base

CONN_STRING = "postgresql+psycopg2://postgres:AmarSinghp#s2s1@43.205.33.196:5432/jrp_db"

def get_engine() -> Engine:
    return create_engine(CONN_STRING, echo=False)


def get_session(engine: Engine) -> Session:
    session = Session(engine)
    return session


def execute_ddl(engine: Engine):
    import app.models  
    Base.metadata.create_all(bind=engine)
