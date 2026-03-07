from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime


class UserBase(BaseModel):
    """Базовая модель пользователя"""
    username: str = Field(min_length=3, max_length=150)
    email: str | None = Field(None, max_length=254)
    first_name: str | None = Field(None, max_length=150)
    last_name: str | None = Field(None, max_length=150)
    is_active: bool = True


class UserCreate(UserBase):
    """Для создания пользователя"""
    password: str = Field(min_length=8)
    email: EmailStr


class UserUpdate(BaseModel):
    """Для обновления данных пользователя"""
    first_name: str | None = Field(None, max_length=150)
    last_name: str | None = Field(None, max_length=150)
    email: EmailStr | None = None
    is_active: bool | None = None


class User(UserBase):
    """Для чтения пользователя из БД (без пароля)"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_superuser: bool
    is_staff: bool
    date_joined: datetime
    last_login: datetime | None = None
    email: str | None = None