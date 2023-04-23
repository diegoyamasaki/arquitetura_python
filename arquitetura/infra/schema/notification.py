from typing import Optional
from pydantic import BaseModel


class NotificationSchemaBase(BaseModel):
    id: str
    message: str
    user_id: str

    class Config:
        orm_mode = True
