from task_manager.models import Task
from datetime import date
import pytest
from pydantic import ValidationError


def test_task_valid():
    task = Task(id=1, title="テスト用タスク", due_date=date(2025, 5, 10))
    assert task.id == 1
    assert task.title == "テスト用タスク"
    assert task.due_date == date(2025, 5, 10)


def test_task_invalid_due_date():
    with pytest.raises(ValidationError):
        Task(id=1, title="テスト用タスク", due_date="invalid-date")
