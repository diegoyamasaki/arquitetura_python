from sqlalchemy.orm import Session
from arquitetura.shared.dependencies import get_db
from fastapi import APIRouter, Depends, status, Response
from arquitetura.application.subscription import SubscriptipnApplication
from arquitetura.infra.schema.subscription import SubscriptionSchemaCreate, SubscriptionSchemaUpdate
from arquitetura.infra.repository.subscription_repository import SubscriptionRepository

subscription_route = APIRouter()


@subscription_route.get("/", status_code=200)
def subscriptions(
        application: SubscriptipnApplication = Depends(SubscriptipnApplication),
        db: Session = Depends(get_db),
        repository: SubscriptionRepository = Depends(SubscriptionRepository)):
    return application.get_all(db, repository)


@subscription_route.post('/', status_code=status.HTTP_201_CREATED)
def post_subscription(
        data: SubscriptionSchemaCreate,
        application: SubscriptipnApplication = Depends(SubscriptipnApplication),
        db: Session = Depends(get_db),
        repository: SubscriptionRepository = Depends(SubscriptionRepository)):
    user = application.create(data, db, repository)
    return user


@subscription_route.put('/{subscription_id}', status_code=status.HTTP_201_CREATED)
def put_subscription(
        subscription_id: str, data: SubscriptionSchemaUpdate,
        application: SubscriptipnApplication = Depends(SubscriptipnApplication),
        db: Session = Depends(get_db),
        repository: SubscriptionRepository = Depends(SubscriptionRepository)):
    user = application.update(subscription_id, data, db, repository)
    return user


@subscription_route.delete('/{subscription_id}', status_code=status.HTTP_201_CREATED)
def delete_subscription(
        subscription_id: str,
        application: SubscriptipnApplication = Depends(SubscriptipnApplication),
        db: Session = Depends(get_db),
        repository: SubscriptionRepository = Depends(SubscriptionRepository)):
    application.delete(subscription_id, db, repository)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
