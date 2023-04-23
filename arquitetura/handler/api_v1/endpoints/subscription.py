from fastapi import APIRouter, Depends, status, Response
from arquitetura.application.subscription import SubscriptipnApplication
from arquitetura.infra.schema.subscription import SubscriptionSchemaCreate, SubscriptionSchemaUpdate

subscription_route = APIRouter()


@subscription_route.get("/", status_code=200)
def subscriptions(application: SubscriptipnApplication = Depends(SubscriptipnApplication)):
    return application.get_all()


@subscription_route.post('/', status_code=status.HTTP_201_CREATED)
def post_subscription(data: SubscriptionSchemaCreate, application: SubscriptipnApplication = Depends(SubscriptipnApplication)):
    user = application.create(data)
    return user


@subscription_route.put('/{subscription_id}', status_code=status.HTTP_201_CREATED)
def put_subscription(subscription_id: str, data: SubscriptionSchemaUpdate, application: SubscriptipnApplication = Depends(SubscriptipnApplication)):
    user = application.update(subscription_id, data)
    return user


@subscription_route.delete('/{subscription_id}', status_code=status.HTTP_201_CREATED)
def delete_subscription(subscription_id: str, application: SubscriptipnApplication = Depends(SubscriptipnApplication)):
    application.delete(subscription_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
