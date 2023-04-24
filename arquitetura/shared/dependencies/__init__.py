from typing import Generator
from arquitetura.infra.database.session import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    db.current_use_id = None
    try:
        yield db
    finally:
        db.close()
