from pydantic import BaseModel
from sqlalchemy.orm import Session
from abc import ABCMeta, abstractmethod


class Repository(metaclass=ABCMeta):

    @abstractmethod
    def create(self, data: BaseModel, db: Session):
        raise NotImplemented

    @abstractmethod
    def update(self, id: str, data: BaseModel, db: Session):
        raise NotImplemented

    @abstractmethod
    def delete(self, id: str, db: Session):
        raise NotImplemented

    @abstractmethod
    def get_all(self, db: Session):
        raise NotImplemented