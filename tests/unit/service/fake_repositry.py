from src.repositories.tasks import TaskDictRepository


class TaskFakeRepository(TaskDictRepository):

    def __init__(self, tasks: list | None = None):
        self.tasks = {task.id_: task for task in tasks} if tasks else {}