from fastapi import APIRouter, Depends, status, Response
from arquitetura.application.user import UserApplcation
from arquitetura.infra.schema.user import UserSchemaCreate, UserSchemaUpdate

user_route = APIRouter()


@user_route.get("/", status_code=200)
def users(application: UserApplcation = Depends(UserApplcation)):
    return application.get_all()


@user_route.post('/', status_code=status.HTTP_201_CREATED)
def post_user(data: UserSchemaCreate, application: UserApplcation = Depends(UserApplcation)):
    user = application.create(data)
    return user


@user_route.put('/{user_id}', status_code=status.HTTP_201_CREATED)
def put_user(user_id: str, data: UserSchemaUpdate, application: UserApplcation = Depends(UserApplcation)):
    user = application.update(user_id, data)
    return user


@user_route.delete('/{user_id}', status_code=status.HTTP_201_CREATED)
def delete_user(user_id: str, user_application: UserApplcation = Depends(UserApplcation)):
    user_application.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
