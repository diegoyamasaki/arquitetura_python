from sqlalchemy.orm import Session
from arquitetura.shared.dependencies import get_db
from arquitetura.application.user import UserApplcation
from fastapi import APIRouter, Depends, status, Response
from arquitetura.infra.schema.user import UserSchemaCreate, UserSchemaUpdate
from arquitetura.infra.repository import Repository
from arquitetura.infra.repository.user_repository import UserRepository

user_route = APIRouter()


@user_route.get("/", status_code=200)
def users(
        application: UserApplcation = Depends(UserApplcation),
        db: Session = Depends(get_db),
        repository: Repository = Depends(UserRepository)):
    return application.get_all(db, repository)


@user_route.post('/', status_code=status.HTTP_201_CREATED)
def post_user(
        data: UserSchemaCreate, application: UserApplcation = Depends(UserApplcation),
        db: Session = Depends(get_db),
        repository: Repository = Depends(UserRepository)):
    user = application.create(data, db, repository)
    return user


@user_route.put('/{user_id}', status_code=status.HTTP_201_CREATED)
def put_user(
        user_id: str,
        data: UserSchemaUpdate, application: UserApplcation = Depends(UserApplcation),
        db: Session = Depends(get_db),
        repository: Repository = Depends(UserRepository)):
    user = application.update(user_id, data, db, repository)
    return user


@user_route.delete('/{user_id}', status_code=status.HTTP_201_CREATED)
def delete_user(
        user_id: str,
        user_application: UserApplcation = Depends(UserApplcation),
        db: Session = Depends(get_db),
        repository: Repository = Depends(UserRepository)):
    user_application.delete(user_id, db, repository)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
