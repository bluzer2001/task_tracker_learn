from fastapi import FastAPI, Depends

from .handlers import task_not_found_handler
from .routers import task_router, user_router
from src.exceptions import TaskNotFoundError

app = FastAPI()

routers = [
    task_router,
    user_router,
]

handlers = {
    TaskNotFoundError: task_not_found_handler
}

for router in routers:
    app.include_router(router)

for error, handler in handlers.items():
    app.add_exception_handler(error, handler)

@app.get("/")
def read_root():
    return {"Hello": "World"}


