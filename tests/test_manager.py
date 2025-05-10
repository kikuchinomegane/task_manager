from task_manager.models import Task
from task_manager.manager import get_next_id, add_task, list_tasks
from datetime import date
from task_manager import storage


def test_get_next_id():
    tasks = [
        Task(id=1, title="A", due_date=date(2025, 5, 10)),
        Task(id=3, title="B", due_date=date(2025, 5, 10)),
    ]
    assert get_next_id(tasks) == 4


def test_get_next_id_if_empty():
    assert get_next_id([]) == 1


def test_add_task(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "STORAGE_FILE", test_file)

    add_task(title="買い物", due_date=date(2025, 5, 11))
    tasks = list_tasks()
    assert tasks[0].title == "買い物"
