from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SubscriptionSchemaBase(BaseModel):
    id: Optional[str]
    user_id: str
    value: int
    product_name: str

    class Config:
        orm_mode = True


class SubscriptionSchemaCreate(SubscriptionSchemaBase):
    subscription_date: datetime


class SubscriptionSchemaUpdate(SubscriptionSchemaBase):
    user_id: Optional[str]
    value: Optional[int]
    product_name: Optional[str]

