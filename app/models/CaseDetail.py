from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, func
from datetime import datetime
from .base import Base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Text,Date
from sqlalchemy.sql import text
from .base import Base

class CaseDetail(Base):
    __tablename__ = "case_details"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    caseno: Mapped[int] = mapped_column(Integer,nullable=True)
    cino: Mapped[str] = mapped_column(String(255), nullable=True)
    fil_no: Mapped[str] = mapped_column(String(255), nullable=True)
    pet_name: Mapped[str] = mapped_column(String(255), nullable=True)
    res_name: Mapped[str] = mapped_column(String(255), nullable=True)
    pet_adv_name: Mapped[str] = mapped_column(String(255), nullable=True)
    res_adv_name: Mapped[str] = mapped_column(String(255), nullable=True)
    petadvenrollment: Mapped[str] = mapped_column(String(255), nullable=True)
    petadvenrollmentyear: Mapped[int] = mapped_column(Integer,nullable=True)
    bench_id: Mapped[int] = mapped_column(Integer,nullable=True)
    fil_dt: Mapped[datetime] = mapped_column(DateTime, server_default=text("now()"), nullable=False)
    case_pages: Mapped[str] = mapped_column(String(255), nullable=False)
    dacode: Mapped[str] = mapped_column(Text, nullable=False)
    conn_key: Mapped[str] = mapped_column(String(255), nullable=True)
    lastorder: Mapped[str] = mapped_column(Text, nullable=True)
    listorder: Mapped[int] = mapped_column(Integer,nullable=False)
    scanstat: Mapped[str] = mapped_column(String(255), nullable=True)
    tentative_cl_dt: Mapped[datetime] = mapped_column(Date, nullable=True)
    delink: Mapped[int] = mapped_column(Integer,nullable=False)
    admitted: Mapped[datetime] = mapped_column(Date, nullable=True)
    caseyear: Mapped[int] = mapped_column(Integer,nullable=True)
    pet_name_h: Mapped[str] = mapped_column(String(255), nullable=True)
    res_name_h: Mapped[str] = mapped_column(String(255), nullable=True)
    pet_adv_h: Mapped[str] = mapped_column(String(255), nullable=True)
    res_adv_h: Mapped[str] = mapped_column(String(255), nullable=True)
    resadven: Mapped[str] = mapped_column(String(255), nullable=True)
    resadvenyr: Mapped[int] = mapped_column(Integer,nullable=True)
    c_status: Mapped[str] = mapped_column(String(255), nullable=True)
    bno: Mapped[int] = mapped_column(Integer,nullable=True)
    prevno: Mapped[str] = mapped_column(String(255), nullable=True)
    prevno_fildt: Mapped[datetime] = mapped_column(Date, nullable=True)
    claim_amt: Mapped[int] = mapped_column(Integer,nullable=True)
    bailno: Mapped[int] = mapped_column(Integer,nullable=True)
    head_code: Mapped[str] = mapped_column(String(255), nullable=True)
    ack_id: Mapped[str] = mapped_column(Integer, nullable=True)
    ack_rec_dt: Mapped[str] = mapped_column(Integer, nullable=True)
    outside: Mapped[str] = mapped_column(String(255), nullable=True)
    court_fee_flag: Mapped[str] = mapped_column(Integer, nullable=True)
    relief: Mapped[str] = mapped_column(String(255), nullable=True)
    law_code: Mapped[str] = mapped_column(Integer, nullable=True)
    law_other: Mapped[str] = mapped_column(String(255), nullable=True)
    usec1: Mapped[str] = mapped_column(String(255), nullable=True)
    desc1: Mapped[str] = mapped_column(String(255), nullable=True)
    fixed: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("now()"), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("now()"), nullable=False)
    created_by: Mapped[str] = mapped_column(Integer, nullable=True)
    updated_by: Mapped[str] = mapped_column(Integer, nullable=True)
    casetype_id: Mapped[str] = mapped_column(Integer, nullable=True)
    district_id: Mapped[str] = mapped_column(Integer, nullable=True)
    establishment_id: Mapped[str] = mapped_column(Integer, nullable=True)
    pet_advocate_id: Mapped[str] = mapped_column(Integer, nullable=True)
    res_advocate_id: Mapped[str] = mapped_column(Integer, nullable=True)
    case_nature_id: Mapped[str] = mapped_column(Integer, nullable=True)




