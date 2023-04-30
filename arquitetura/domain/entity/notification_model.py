from datetime import datetime
from arquitetura.shared.config import settings
from sqlalchemy import Column, String, DATETIME, BOOLEAN, Integer


class NotificationModel(settings.DBModel):
    __tablename__ = "notification"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    notification_id: str = Column(String)
    user_document: str = Column(String)
    notification_message: str = Column(String)
    sended: bool = Column(BOOLEAN)
    create_ad: datetime = Column(DATETIME)
    deleted_at: datetime = Column(DATETIME)
