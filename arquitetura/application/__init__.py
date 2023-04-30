from pydantic import BaseModel
from abc import ABCMeta, abstractmethod


class Application(metaclass=ABCMeta):

    @abstractmethod
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
