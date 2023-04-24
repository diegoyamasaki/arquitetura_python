from datetime import datetime
from arquitetura.shared.config import settings
from sqlalchemy import Column, Integer, String, DATETIME, FLOAT


class SubscriptionModel(settings.DBModel):
    __tablename__ = "subscription"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_document: str = Column(String)
    subscription_id: str = Column(String)
    purchase_at: datetime = Column(DATETIME)
    purchase_value: float = Column(FLOAT)
    order_number: int = Column(Integer)
    deleted_at: datetime = Column(DATETIME)

