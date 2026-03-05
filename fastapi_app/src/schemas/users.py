from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime


class UserBase(BaseModel):
    """Базовая модель пользователя"""
    username: str = Field(min_length=3, max_length=150)
    email: EmailStr
    first_name: str | None = Field(None, max_length=150)
    last_name: str | None = Field(None, max_length=150)


class UserCreate(UserBase):
    """Для создания пользователя"""
    password: str


class User(UserBase):
    """Для чтения пользователя из БД"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_active: bool = True
    date_joined: datetime
    last_login: datetime | None = None