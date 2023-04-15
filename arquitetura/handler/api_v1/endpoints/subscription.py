from fastapi import APIRouter

subscription_route = APIRouter()


@subscription_route.get("/", status_code=200)
def subscriptions():
    return {"message": "subscriptionroute"}
