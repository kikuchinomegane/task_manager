from task_manager.models import Task
from task_manager.storage import save_tasks, load_tasks
from datetime import date


def get_next_id(tasks: list[Task]) -> int:
    return max((task.id for task in tasks), default=0) + 1


def add_task(title: str, due_date: date):
    tasks = load_tasks()

    new_id = get_next_id(tasks)
    task = Task(id=new_id, title=title, due_date=due_date)
    tasks.append(task)

    save_tasks(tasks)


def list_tasks() -> list[Task]:
    return load_tasks()
