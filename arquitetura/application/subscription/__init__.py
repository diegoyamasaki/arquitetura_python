from pydantic import BaseModel
from arquitetura.application import Application


class SubscriptipnApplication(Application):

    def create(self, data: BaseModel):
        pass

    def update(self, id: str, data: BaseModel):
        pass

    def delete(self, id: str):
        pass

    def get_all(self):
        pass
