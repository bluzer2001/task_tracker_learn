from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse

from src.exceptions import TaskNotFoundError


def task_not_found_handler(request: Request, exc: TaskNotFoundError):
    # raise HTTPException(status_code=404, detail="Task not found")
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail": "Task not found",
        },
    )