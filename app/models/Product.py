from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, func
from .base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)

    # category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    # user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    category_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    parent_id = Column(Integer, nullable=True)
    specification = Column(String, nullable=True)

    status = Column(
        Enum("active", "inactive", "dump", "dispose", name="product_status"),
        default="active",
        nullable=False,
    )

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
