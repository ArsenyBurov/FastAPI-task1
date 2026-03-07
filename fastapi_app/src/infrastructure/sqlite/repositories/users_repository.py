from typing import Optional, List
from sqlalchemy.orm import Session
from src.infrastructure.sqlite.models.users import User  # только это


class UsersRepository:
    def __init__(self):
        self.model = User

    def get_by_id(self, session: Session, user_id: int) -> Optional[User]:
        return session.get(self.model, user_id)

    def get_by_username(self, session: Session, username: str) -> Optional[User]:
        return session.query(self.model).filter(self.model.username == username).first()

    def get_all(self, session: Session) -> List[User]:
        return session.query(self.model).all()