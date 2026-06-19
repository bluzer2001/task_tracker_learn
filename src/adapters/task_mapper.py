from src.models import Task
from src.database.models import Task as TaskModel



class TaskMapper:

    @staticmethod
    def to_model(task: Task) -> TaskModel:
        return TaskModel(
            id_=task.id_,
            name=task.name,
            is_closed=task.is_closed,
            deadline=task.deadline,
            tags=task.tags,
        )

    @staticmethod
    def many_to_model(tasks: list[Task]):
        return [TaskMapper.to_model(task) for task in tasks]

    @staticmethod
    def to_entity(task: TaskModel) -> Task:
        return Task(
            id_=task.id_,
            name=task.name,
            is_closed=task.is_closed,
            deadline=task.deadline,
            tags=task.tags
        )

    @staticmethod
    def many_to_entity(tasks: list[TaskModel]):
        return [TaskMapper.to_entity(task) for task in tasks]