from arquitetura.shared.config import settings


class UserModel(settings.DBModel):
    __tablename__ = 'user'
