from fastapi import FastAPI, HTTPException, status

app = FastAPI()


tasks = [
    {
        "id": 1,
        "name": "Изучить HTTP",
        "is_closed": False,
    },
    {
        "id": 2,
        "name": "Изучить FastAPI",
        "is_closed": False,
    },
]


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/tasks")
def read_tasks(is_closed: bool | None = None):
    if is_closed is not None:
        return [task for task in tasks if task["is_closed"] == is_closed]
    return tasks

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    try:
        return next(task for task in tasks if task["id"] == task_id)
    except StopIteration:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")