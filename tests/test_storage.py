from task_manager.models import Task
from datetime import date
from task_manager import storage
from task_manager.storage import save_tasks, load_tasks


# タスクを保存→読み込みして、正しく復元されること
def test_save_and_load_tasks(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "STORAGE_FILE", test_file)

    task = Task(id=1, title="買い物", due_date=date(2025, 5, 11))
    save_tasks([task])
    tasks = load_tasks()
    assert tasks[0].id == 1
    assert tasks[0].title == "買い物"


# ファイルが存在しないときに空リストを返すこと
def test_load_tasks_returns_empty_on_no_file(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "STORAGE_FILE", test_file)

    tasks = load_tasks()
    assert tasks == []
