from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_STR_V1 = "/api/v1"
    DBModel = declarative_base()
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"


settings = Settings()
