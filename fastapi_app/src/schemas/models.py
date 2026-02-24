from pydantic import BaseModel, EmailStr, Field, SecretStr
from datetime import datetime

class UserBase(BaseModel):
    """Базовая модель пользователя"""
    username: str = Field(min_length=3, max_length=150)
    email: EmailStr
    first_name: str | None = Field(None, max_length=150)
    last_name: str | None = Field(None, max_length=150)

class Category(BaseModel):
    """Базовая модель категории"""
    title: str = Field(max_length=256)
    description: str
    slug: str = Field(
        max_length=64,
        pattern=r'^[a-zA-Z0-9_-]+$'
    )
    is_published: bool = True

class Location(BaseModel):
    """Базовая модель местоположения"""
    name: str = Field(max_length=256)
    is_published: bool = True

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

class Comment(BaseModel):
    """Базовая модель комментария"""
    text: str
    post_id: int
    author_id: int
    created_at: datetime = Field(default_factory=datetime.now, frozen=True)