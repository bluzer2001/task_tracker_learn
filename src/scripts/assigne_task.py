from src.service import TaskUserService
from src.repositories import TaskAlchemyRepository, UserAlchemyRepository
from src.database.sqllite import session_factory, init_and_clear_db
from src.models import User, Task


def assign_to_user():
    session = session_factory()
    task_repo = TaskAlchemyRepository(session)
    user_repo = UserAlchemyRepository(session)
    task_user_service = TaskUserService(task_repo, user_repo)

    user = User(name="test_user", email="example")
    task = Task(name="test_task")

    with init_and_clear_db():
        user_repo.save(user)
        task_repo.save(task)
        return task_user_service.assigne_task_to_user(task_id=task.id_, user_id=user.id_), user
