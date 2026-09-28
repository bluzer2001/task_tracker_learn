import uuid

from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.dependencies import get_task_service, get_task_repository
from src.api.schemas import TaskCreateSchema, TaskUpdateSchema, TaskDetailsSchema
from src.repositories.tasks import TaskAlchemyRepository
from src.service.tasks import TasksService
from src.database.sqllite import session_factory, get_session

router = APIRouter(prefix="/tasks", tags=["tasks"])

    
    
@router.get("/")
def read_tasks(is_closed: bool | None = None, service: TasksService = Depends(get_task_service)):
    return service.get_tasks(is_closed=is_closed)


@router.get("/{task_id}", response_model=TaskDetailsSchema)
def read_task(task_id: uuid.UUID, repo: TaskAlchemyRepository = Depends(get_task_repository)):
    return repo.get_by_id(task_id)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(
    task: TaskCreateSchema, service: TasksService = Depends(get_task_service)
):
    new_task = service.create(**task.model_dump())
    return new_task


@router.patch("/{task_id}")
def update_task(task_id: uuid.UUID, data: TaskUpdateSchema, service: TasksService = Depends(get_task_service)):
    return service.update(task_id, **data.model_dump(exclude_unset=True))


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    task = find_task_by_id(task_id)
    tasks.remove(task)