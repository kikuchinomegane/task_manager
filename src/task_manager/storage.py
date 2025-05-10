from pathlib import Path
import json
from task_manager.models import Task

STORAGE_FILE = Path("tasks.json")


def save_tasks(tasks: list[Task]) -> None:
    with STORAGE_FILE.open("w", encoding="utf-8") as f:
        json.dump(
            [task.model_dump(mode="json") for task in tasks],
            f,
            ensure_ascii=False,
            indent=2,
        )


def load_tasks() -> list[Task]:
    if not STORAGE_FILE.exists():
        return []

    with STORAGE_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
        return [Task(**item) for item in data]
