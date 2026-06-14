from src.models import Task
import factory


class TaskFactory(factory.Factory):

    class Meta:
        model = Task

    name = factory.Faker("sentence")
    deadline = factory.Faker("date_time")
    is_closed = factory.Faker("boolean")
    tags = factory.Faker("pylist", allowed_types=[str])
    id_ = factory.Faker("uuid4")


if __name__ == "__main__":
    task = TaskFactory()
    print(task)