from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Session

from arquitetura.infra.repository import Repository
from arquitetura.domain.entity.user_model import UserModel


class UserRepository(Repository):
    def create(self, data: BaseModel, db: Session) -> UserModel:
        pass

    def update(self, id: str, data: BaseModel, db: Session) -> UserModel:
        pass

    def delete(self, id: str, db: Session) -> None:
        pass

    def get_all(self, db: Session) -> List[UserModel]:
        pass
