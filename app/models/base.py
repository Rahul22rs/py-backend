from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, String, MetaData, Float,ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass