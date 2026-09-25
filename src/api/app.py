from fastapi import FastAPI, Depends
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


def return_1():
    return 1

def return_2(number: int = Depends(return_1)):
    return number*2

@app.get("/test")
def test_route(number: int = Depends(return_2)):
    return {"number": number}
