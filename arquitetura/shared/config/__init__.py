from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_STR_V1 = "/api/v1"
    DBModel = declarative_base()


settings = Settings()
