from fastapi import FastAPI
from .routers import task_router, user_router

app = FastAPI()

routers = [
    task_router,
    user_router,
]

for router in routers:
    app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
