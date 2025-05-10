import argparse
from task_manager.manager import add_task, list_tasks
from datetime import datetime


def parse_date(date_str: str):
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def run_cli():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # "Add" subcommands
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--title", required=True)
    add_parser.add_argument("--due_date", type=parse_date, required=False)

    # "List" subcommands
    add_parser = subparsers.add_parser("list")

    args = parser.parse_args()

    if args.command == "add":
        add_task(title=args.title, due_date=args.due_date)
    elif args.command == "list":
        tasks = list_tasks()
        if not tasks:
            print("タスクはありません")

        for task in tasks:
            print(f"[{task.id}] {task.title} - {task.due_date}")
