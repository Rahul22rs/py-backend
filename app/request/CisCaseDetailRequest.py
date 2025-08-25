from pydantic import BaseModel #Defines request/response schemas with validation.
from typing import Optional, Literal

class CisCaseDetailRequest(BaseModel):
    product_name: str
    category_id: int
    user_id: int
    parent_id: int
    specification: Optional[str] = None