from src.repositories.tasks import TaskListRepository, TaskDictRepository, TaskAlchemyRepository
from src.service import TasksService
from datetime import datetime

from src.database.models import Base, TaskModel
from src.database.sqllite import get_engine, session_factory
from sqlalchemy import select
from src.scripts.assigne_task import assign_to_user


def main():
    # repository = TaskListRepository()
    # service = TasksService(repository)
    #
    #
    # task_names = ["Task1", "Task2"]
    # deadlines = [datetime(2026, 6, 12, 12, 00, 00),
    #              datetime(2026, 9, 12, 12, 00, 00)]
    #
    # for task, deadline in zip(task_names, deadlines):
    #     repository.create(task, deadline)
    #
    # active_tasks = service.get_active_tasks()
    #
    # print(active_tasks)
    #
    # service.close_task_by_id(active_tasks[0].id_)
    #
    # active_tasks = service.get_active_tasks()
    #
    # print(active_tasks)
    #
    # start_date = datetime(2026, 5, 12, 12, 00, 00)
    # end_date = datetime(2026, 8, 12, 12, 00, 00)
    # filtered = service.get_tasks_by_deadline(start_date=start_date, end_date=end_date)
    # print(filtered)

    # ---

    # engine = get_engine()
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    #
    # repository = TaskAlchemyRepository(session_factory())
    #
    #
    # repository.create("test1")
    # repository.create("test2")
    # tasks = repository.get_all()
    # print(tasks)

    # service = TasksService(repository)
    # active_tasks = service.get_active_tasks()
    # print(active_tasks)
    # print(active_tasks[0].id_)
    # service.close_task_by_id(active_tasks[0].id_)
    # active_tasks = service.get_active_tasks()
    # print(active_tasks)

    # ---
    # repository = TaskDictRepository()
    # repository.create("test1")
    # repository.create("test2")
    # tasks = repository.get_all()
    # print(tasks)
    # task = tasks[0]
    # task = repository.update_task(task.id_, is_closed=True)
    # filtered = repository.filter(is_closed=False)
    # print(filtered, task)
    task, user = assign_to_user()
    print(task.assignee_id, user.id_)

if __name__ == '__main__':

    main()
