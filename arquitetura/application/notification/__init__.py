from pydantic import BaseModel
from sqlalchemy.orm import Session

from  arquitetura.application import Application
from arquitetura.infra.repository.notification_repository import NotificationRepository


class NotificationApplication(Application):

    def create(self, data: BaseModel, db: Session, repository: NotificationRepository):
        return repository.create(data, db)

    def delete(self, id: str, db: Session, repository: NotificationRepository):
        return repository.delete(id, db)

    def get_all(self, db: Session, repository: NotificationRepository):
        return repository.get_all(db)
