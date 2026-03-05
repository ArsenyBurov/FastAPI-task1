from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class LocationBase(BaseModel):
    """Базовая модель местоположения"""
    name: str = Field(max_length=256)
    is_published: bool = True


class LocationCreate(LocationBase):
    """Для создания новой локации"""
    pass


class Location(LocationBase):
    """Для чтения локации из БД"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime