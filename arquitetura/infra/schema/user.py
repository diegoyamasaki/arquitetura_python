from typing import Optional
from pydantic import BaseModel, EmailStr


class UserSchemaBase(BaseModel):
    id: Optional[str]
    name: str
    surname: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserSchemaCreate(UserSchemaBase):
    password: str


class UserSchemaUpdate(UserSchemaBase):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
