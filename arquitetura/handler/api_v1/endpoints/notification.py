from fastapi import APIRouter, Depends, status, Response
from arquitetura.application.notification import NotificationApplication
from arquitetura.infra.schema.notification import NotificationSchemaBase

notification_route = APIRouter()


@notification_route.get("/", status_code=200)
def notifications(
        application: NotificationApplication
        = Depends(NotificationApplication)):
    return application.get_all()


@notification_route.post('/', status_code=status.HTTP_201_CREATED)
def post_notification(
        data: NotificationSchemaBase,
        application: NotificationApplication
        = Depends(NotificationApplication)):
    user = application.create(data)
    return user


@notification_route.delete(
    '/{notification_id}',
    status_code=status.HTTP_201_CREATED)
def delete_notification(
        notification_id: str,
        application: NotificationApplication
        = Depends(NotificationApplication)):
    application.delete(notification_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
