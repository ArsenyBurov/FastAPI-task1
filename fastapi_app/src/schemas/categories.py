from pydantic import BaseModel, Field

class Category(BaseModel):
    """Базовая модель категории"""
    title: str = Field(max_length=256)
    description: str
    slug: str = Field(
        max_length=64,
        pattern=r'^[a-zA-Z0-9_-]+$'
    )
    is_published: bool = True