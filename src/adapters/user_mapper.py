__all__ = ("UserMapper", )

from src.models import User
from src.database.models import UserModel



class UserMapper:

    @staticmethod
    def to_model(user: User) -> UserModel:
        return UserModel(
            id_=user.id_,
            name=user.name,
            is_blocked=user.is_blocked,
            email=user.email
        )

    @staticmethod
    def many_to_model(users: list[User]) -> list[UserModel]:
        return [UserMapper.to_model(user) for user in users]

    @staticmethod
    def update_model(entity: User, model: UserModel):
        model.id_ = entity.id_
        model.name = entity.name
        model.is_blocked = entity.is_blocked
        model.email = entity.email

    @staticmethod
    def to_entity(user: UserModel) -> User:
        return User(
            id_=user.id_,
            name=user.name,
            is_blocked=user.is_blocked,
            email=user.email
        )

    @staticmethod
    def many_to_entity(users: list[UserModel]) -> list[User]:
        return [UserMapper.to_entity(user) for user in users]
