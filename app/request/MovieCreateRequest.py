from pydantic import BaseModel
class MovieCreateRequest(BaseModel):
    name: str
    rating: float