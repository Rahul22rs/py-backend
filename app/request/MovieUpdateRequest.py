from pydantic import BaseModel,Field
class MovieUpdateRequest(BaseModel):
    name: str
    rating: float