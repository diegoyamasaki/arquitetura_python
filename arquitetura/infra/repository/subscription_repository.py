from typing import List

from pydantic import BaseModel
from sqlalchemy.orm import Session

from arquitetura.infra.repository import Repository
from arquitetura.domain.entity.subscription_model import SubscriptionModel


class SubscriptionRepository(Repository):

    def create(self, data: BaseModel, db: Session) -> SubscriptionModel:
        pass

    def update(self, id: str, data: BaseModel, db: Session) -> SubscriptionModel:
        pass

    def delete(self, id: str, db: Session) -> None:
        pass

    def get_all(self, db: Session) -> List[SubscriptionModel]:
        pass
