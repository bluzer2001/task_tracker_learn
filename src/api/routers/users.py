from fastapi import HTTPException, status, APIRouter
from src.api.schemas import UserCreateSchema, UserUpdateSchema

router = APIRouter(prefix="/users", tags=["users"])

users = [
    {
        "id": 1,
        "name": "Alex",
        "is_blocked": False,
    },
    {
        "id": 2,
        "name": "Ivan",
        "is_blocked": True,
    },
]


def find_user_by_id(user_id: int):
    try:
        return next(user for user in users if user["id"] == user_id)
    except StopIteration:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    


@router.get("/")
def read_users(is_blocked: bool | None = None):
    if is_blocked is not None:
        return [user for user in users if user["is_blocked"] == is_blocked]
    return users


@router.get("/{user_id}")
def read_user(user_id: int):
    return find_user_by_id(user_id)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreateSchema):
    new_user = {
        "id": len(users) + 1,
        **user.model_dump(),
    }
    users.append(new_user)
    return new_user


@router.patch("/{user_id}")
def update_user(user_id: int, data: UserUpdateSchema):
    user = find_user_by_id(user_id)
    user.update(**data.model_dump(exclude_unset=True))
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    user = find_user_by_id(user_id)
    users.remove(user)
