import uuid

from fastapi import HTTPException, status, APIRouter, Depends

from src.exceptions import TaskNotFoundError
from src.api.dependencies import get_task_service
from src.api.schemas import TaskUpdateSchema, TaskCreateSchema, TaskDetailsSchema
from src.service.tasks import TasksService

router = APIRouter(prefix="/tasks", tags=["tasks"])

    
    
@router.get("/", response_model=list[TaskDetailsSchema])
def read_tasks(is_closed: bool | None = None, service: TasksService = Depends(get_task_service)):
    return service.get_tasks(is_closed=is_closed)


@router.get("/{task_id}", response_model=TaskDetailsSchema)
def read_task(task_id: uuid.UUID, service: TasksService = Depends(get_task_service)):
    return service.get(task_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TaskDetailsSchema)
def create_task(
    task: TaskCreateSchema, service: TasksService = Depends(get_task_service)
):
    new_task = service.create(**task.model_dump())
    return new_task


@router.patch("/{task_id}", response_model=TaskDetailsSchema)
def update_task(task_id: uuid.UUID, data: TaskUpdateSchema, service: TasksService = Depends(get_task_service)):
    return service.update(task_id, **data.model_dump(exclude_unset=True))


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: uuid.UUID, service: TasksService = Depends(get_task_service)):
    service.delete(task_id)