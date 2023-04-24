from sqlalchemy.orm import Session
from arquitetura.shared.dependencies import get_db
from fastapi import APIRouter, Depends, status, Response
from arquitetura.application.notification import NotificationApplication
from arquitetura.infra.schema.notification import NotificationSchemaBase
from arquitetura.infra.repository.notification_repository import NotificationRepository

notification_route = APIRouter()


@notification_route.get("/", status_code=200)
def notifications(
        application: NotificationApplication = Depends(NotificationApplication),
        db: Session = Depends(get_db),
        repository: NotificationRepository = Depends(NotificationRepository)):
    return application.get_all(db, repository)


@notification_route.post('/', status_code=status.HTTP_201_CREATED)
def post_notification(
        data: NotificationSchemaBase,
        application: NotificationApplication = Depends(NotificationApplication),
        db: Session = Depends(get_db), repository: NotificationRepository = Depends(NotificationRepository)):
    return application.create(data, db, repository)


@notification_route.delete('/{notification_id}', status_code=status.HTTP_201_CREATED)
def delete_notification(
        notification_id: str,
        application: NotificationApplication = Depends(NotificationApplication),
        db: Session = Depends(get_db),
        repository: NotificationRepository = Depends(NotificationRepository)):
    application.delete(notification_id, db, repository)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
