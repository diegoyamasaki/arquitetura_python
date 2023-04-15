from fastapi import FastAPI
from arquitetura.shared.config import settings
from arquitetura.handler.api_v1.api import api_router

app = FastAPI()

app.include_router(api_router, prefix=settings.API_STR_V1)


@app.get("/")
def root():
    return {"message": "Arquitetura Python"}
