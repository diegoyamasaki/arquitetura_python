from pydantic import BaseModel
from sqlalchemy.orm import Session
from arquitetura.application import Application
from arquitetura.infra.repository.user_repository import UserRepository



class UserApplcation(Application):

    def create(self, data: BaseModel, db: Session, repository: UserRepository):
        return repository.create(data, db)

    def update(self, id: str, data: BaseModel, db: Session, repository: UserRepository):
        return repository.update(id, data, db)

    def delete(self, id: str, db: Session, repository: UserRepository):
        return repository.delete(id, db)

    def get_all(self, db: Session, repository: UserRepository):
        return repository.get_all(db)

