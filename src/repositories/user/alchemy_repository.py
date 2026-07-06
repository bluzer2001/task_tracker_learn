__all__ = ("UserAlchemyRepository", )


from sqlalchemy.orm import Session
from src.adapters import UserMapper
from src.models import User
from src.database.models import UserModel
from src.repositories.base import BaseRepository


class UserAlchemyRepository(BaseRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: str):
        user_model = self.session.get(UserModel, user_id)
        if user_model:
            return UserMapper.to_entity(user_model)
        return None

    def get_all(self):
        user_models = self.session.query(UserModel).all()
        return UserMapper.many_to_entity(user_models)

    def save(self, user: User):
        user_model = UserMapper.to_model(user)
        self.session.add(user_model)
        self.session.commit()
        user.id_ = user_model.id_
