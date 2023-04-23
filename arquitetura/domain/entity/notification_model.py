from datetime import datetime
from arquitetura.shared.config import settings
from sqlalchemy import Column, String, DATETIME, BOOLEAN


class NotificationModel(settings.DBModel):
    __tablename__ = "notification"

    notification_id: str = Column(String, primary_key=True)
    user_document: str = Column(String)
    notification_message: str = Column(String)
    sended: bool = Column(BOOLEAN)
    create_ad: datetime = Column(DATETIME)
    deleted_at: datetime = Column(DATETIME)

