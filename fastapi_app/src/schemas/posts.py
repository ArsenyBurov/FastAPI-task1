from pydantic import BaseModel, Field
from datetime import datetime

class Post(BaseModel):
    """Базовая модель поста"""
    title: str = Field(max_length=256)
    text: str
    pub_date: datetime
    author_id: int
    location_id: int | None = None
    category_id: int | None = None
    image: str | None = None
    is_published: bool = True