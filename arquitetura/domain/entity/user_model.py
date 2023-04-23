from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DATETIME
from arquitetura.shared.config import settings


class UserModel(settings.DBModel):
    __tablename__ = 'user'
    document: str = Column(String, primary_key=True)
    name: str = Column(String)
    surname: str = Column(String)
    email: str = Column(String)
    age: int = Column(Integer)
    active: bool = Column(Boolean)
    created_at: datetime = Column(DATETIME)
    updated_at: datetime = Column(DATETIME)
    deleted_at: datetime = Column(DATETIME)

