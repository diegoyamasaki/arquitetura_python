from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from arquitetura.shared.config import Settings


engine = create_engine(Settings.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False},)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
