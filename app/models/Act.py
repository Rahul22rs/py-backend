from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, func
from datetime import datetime
from .base import Base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Text
from sqlalchemy.sql import text
from .base import Base

class Act(Base):
    __tablename__ = "act_t"

    actcode: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    actname: Mapped[str] = mapped_column(String(255), nullable=True)
    lactname: Mapped[str] = mapped_column(String(255), nullable=True)
    acttype: Mapped[str] = mapped_column(Text, nullable=True)
    display: Mapped[str] = mapped_column(Text, nullable=True)
    national_code: Mapped[str] = mapped_column(String(255), nullable=True)
    shortact: Mapped[str] = mapped_column(String(255), nullable=True)
    amd: Mapped[str] = mapped_column(String(255), nullable=True)
    est_code_src: Mapped[str] = mapped_column(String(255), nullable=True)
    create_modify: Mapped[datetime] = mapped_column(DateTime, server_default=text("now()"), nullable=False)