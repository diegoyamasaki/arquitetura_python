from fastapi import APIRouter
from arquitetura.handler.api_v1.endpoints.user import user_route
from arquitetura.handler.api_v1.endpoints.subscription import subscription_route
from arquitetura.handler.api_v1.endpoints.notification import notification_route

api_router = APIRouter()

api_router.include_router(user_route, prefix="/user", tags=["User"])
api_router.include_router(subscription_route, prefix="/subscription", tags=["Subscription"])
api_router.include_router(notification_route, prefix="/notification", tags=["Notification"])
