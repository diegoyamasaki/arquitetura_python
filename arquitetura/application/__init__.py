from pydantic import BaseModel
from sqlalchemy.orm import Session
from abc import ABCMeta, abstractmethod
from arquitetura.infra.repository import Repository


class Application(metaclass=ABCMeta):

    @abstractmethod
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