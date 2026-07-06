from src.models import Task
from src.database.models import TaskModel as AlchemyTask
import factory
import uuid
from tests.session_for_test import session_factory


class TaskFactory(factory.Factory):

    class Meta:
        model = Task

    name = factory.Faker("sentence")
    deadline = factory.Faker("date_time")
    is_closed = factory.Faker("boolean")
    tags = factory.Faker("pylist", allowed_types=[str])
    id_ = factory.Faker("uuid4")


class TaskAlchemyFactory(TaskFactory, factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = AlchemyTask
        sqlalchemy_session_factory = session_factory
        sqlalchemy_session_persistence = "commit"

    id_ = factory.LazyFunction(uuid.uuid4)


if __name__ == "__main__":
    task = TaskFactory()
    print(task)