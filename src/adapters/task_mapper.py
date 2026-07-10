__all__ = ("TaskMapper", )

from src.models import Task
from src.database.models import TaskModel



class TaskMapper:

    @staticmethod
    def to_model(entity: Task) -> TaskModel:
        return TaskModel(
            id_=entity.id_,
            name=entity.name,
            is_closed=entity.is_closed,
            deadline=entity.deadline,
            tags=entity.tags,
            assignee_id=entity.assignee_id
        )

    @staticmethod
    def many_to_model(entitties: list[Task]):
        return [TaskMapper.to_model(entity) for entity in entitties]
    
    @staticmethod
    def update_model(entity: Task, model: TaskModel):
        model.name = entity.name
        model.is_closed = entity.is_closed
        model.deadline = entity.deadline
        model.assignee_id = entity.assignee_id
        model.tags = entity.tags
        

    @staticmethod
    def to_entity(model: TaskModel) -> Task:
        return Task(
            id_=model.id_,
            name=model.name,
            is_closed=model.is_closed,
            deadline=model.deadline,
            tags=model.tags,
            assignee_id=model.assignee_id,
        )

    @staticmethod
    def many_to_entity(models: list[TaskModel]):
        return [TaskMapper.to_entity(model) for model in models]