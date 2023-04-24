from typing import List

from pydantic import BaseModel
from sqlalchemy.orm import Session

from arquitetura.infra.repository import Repository
from arquitetura.domain.entity.notification_model import NotificationModel


class NotificationRepository(Repository):
    def create(self, data: BaseModel, db: Session) -> NotificationModel:
        pass

    def update(self, id: str, data: BaseModel, db: Session) -> NotificationModel:
        pass

    def delete(self, id: str, db: Session) -> None:
        pass

    def get_all(self, db: Session) -> List[NotificationModel]:
        pass
