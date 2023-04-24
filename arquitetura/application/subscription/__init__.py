from pydantic import BaseModel
from sqlalchemy.orm import Session

from  arquitetura.application import Application
from arquitetura.infra.repository.subscription_repository import SubscriptionRepository


class SubscriptipnApplication(Application):

    def create(self, data: BaseModel, db: Session, repository: SubscriptionRepository):
        return repository.create(data, db)

    def update(self, id: str, data: BaseModel, db: Session, repository: SubscriptionRepository):
        return  repository.update(id, data, db)

    def delete(self, id: str, db: Session, repository: SubscriptionRepository):
        return repository.delete(id, db)

    def get_all(self, db: Session, repository: SubscriptionRepository):
        return repository.get_all(db)
