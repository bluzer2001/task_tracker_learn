from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session

from api.dependencies.repo.task import get_task_repository
from src.api.schemas import TaskCreateSchema, TaskUpdateSchema, TaskDetailsSchema
from src.repositories.tasks import TaskAlchemyRepository
from src.service.tasks import TasksService
from src.database.sqllite import session_factory, get_session

router = APIRouter(prefix="/tasks", tags=["tasks"])


def find_task_by_id(task_id: int):
    try:
        return next(task for task in tasks if task["id"] == task_id)
    except StopIteration:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    
@router.get("/")
def read_tasks(is_closed: bool | None = None, repo: TaskAlchemyRepository = Depends(get_task_repository)):
    task_service = TasksService(repo)
    return task_service.get_tasks(is_closed=is_closed)

#
# @router.get("/{task_id}", response_model=TaskDetailsSchema)
# def read_task(task_id: int):
#     return find_task_by_id(task_id)
#
#
# @router.post("/", status_code=status.HTTP_201_CREATED)
# def create_task(task: TaskCreateSchema):
#     new_task = {
#         "id": len(tasks) + 1,
#         **task.model_dump(),
#     }
#     tasks.append(new_task)
#     return new_task
#
#
# @router.patch("/{task_id}")
# def update_task(task_id: int, data: TaskUpdateSchema):
#     task = find_task_by_id(task_id)
#     task.update(**data.model_dump(exclude_unset=True))
#     return task
#
#
# @router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_task(task_id: int):
#     task = find_task_by_id(task_id)
#     tasks.remove(task)