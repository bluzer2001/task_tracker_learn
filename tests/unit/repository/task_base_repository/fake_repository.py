from src.repositories.tasks import TaskBaseRepository

class TaskFakeRepository(TaskBaseRepository):

    def save(self, *args, **kwargs):
        pass

    def get_by_id(self, *args, **kwargs):
        pass

    def get_all(self, *args, **kwargs):
        pass