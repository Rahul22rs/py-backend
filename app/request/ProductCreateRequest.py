from pydantic import BaseModel
class ProductCreateRequest(BaseModel):
    product_name: str