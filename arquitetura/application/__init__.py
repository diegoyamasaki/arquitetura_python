from pydantic import BaseModel
from sqlalchemy.orm import Session
from abc import ABCMeta, abstractmethod
from arquitetura.infra.repository import Repository


class Application(metaclass=ABCMeta):

    @abstractmethod
<<<<<<< HEAD
    def create(self, data: BaseModel):
        raise NotImplementedError

    @abstractmethod
    def update(self, id: str, data: BaseModel):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError
=======
    def create(self, data: BaseModel, db: Session, repository: Repository):
        raise NotImplemented

    @abstractmethod
    def update(self, id: str, data: BaseModel, db: Session, repository: Repository):
        raise NotImplemented

    @abstractmethod
    def delete(self, id: str, db: Session, repository: Repository):
        raise NotImplemented

    @abstractmethod
    def get_all(self, db: Session, repository: Repository):
        raise NotImplemented
>>>>>>> 31ae79f034c33e92e815dca718f2f7b7cdd531d0
