from fastapi import APIRouter

notification_route = APIRouter()


@notification_route.get("/", status_code=200)
def notifications():
    return {"message": "notification route"}
