from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    """Базовая модель пользователя"""
    username: str = Field(min_length=3, max_length=150)
    email: EmailStr
    first_name: str | None = Field(None, max_length=150)
    last_name: str | None = Field(None, max_length=150)