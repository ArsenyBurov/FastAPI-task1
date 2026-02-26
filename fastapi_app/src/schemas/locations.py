from pydantic import BaseModel, Field

class Location(BaseModel):
    """Базовая модель местоположения"""
    name: str = Field(max_length=256)
    is_published: bool = True