from src.models import User
from src.database.models import UserModel as AlchemyUser
import factory
import uuid
from tests.session_for_test import session_factory


class UserFactory(factory.Factory):

    class Meta:
        model = User

    name = factory.Faker("sentence")
    is_blocked = factory.Faker("boolean")
    email = factory.Faker("email")
    id_ = factory.LazyFunction(uuid.uuid4)


class UserAlchemyFactory(UserFactory, factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = AlchemyUser
        sqlalchemy_session_factory = session_factory
        sqlalchemy_session_persistence = "commit"


if __name__ == "__main__":
    task = UserFactory()
    print(task)