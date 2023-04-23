from pydantic import BaseModel
from abc import ABCMeta, abstractmethod


class Application(metaclass=ABCMeta):

    @abstractmethod
    def create(self, data: BaseModel):
        raise NotImplemented

    @abstractmethod
    def update(self, id: str, data: BaseModel):
        raise NotImplemented

    @abstractmethod
    def delete(self, id: str):
        raise NotImplemented

    @abstractmethod
    def get_all(self):
        raise NotImplemented