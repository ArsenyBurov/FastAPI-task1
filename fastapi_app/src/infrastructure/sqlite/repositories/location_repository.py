from typing import Optional, List
from sqlalchemy.orm import Session
from src.infrastructure.sqlite.models.location import Location


class LocationRepository:
    def __init__(self):
        self.model = Location

    def get_by_id(self, session: Session, location_id: int) -> Optional[Location]:
        """Получить локацию по ID"""
        return session.get(self.model, location_id)

    def get_all(self, session: Session) -> List[Location]:
        """Получить все локации"""
        return session.query(self.model).all()

    def get_published(self, session: Session) -> List[Location]:
        """Получить только опубликованные локации"""
        return session.query(self.model).filter(self.model.is_published == True).all()