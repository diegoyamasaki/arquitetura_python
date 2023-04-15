from fastapi import APIRouter

user_route = APIRouter()


@user_route.get("/", status_code=200)
def users():
    return {"message": "user route"}
