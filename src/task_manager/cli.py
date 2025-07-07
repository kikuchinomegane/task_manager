import argparse
import sys
from task_manager.manager import add_task, list_tasks
from datetime import datetime


def parse_date(date_str: str):
    """Parse date string to date object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as e:
        raise argparse.ArgumentTypeError(
            f"Invalid date format: {date_str}. Use YYYY-MM-DD format."
        ) from e


def handle_add_command(args):
    """Handle the add command."""
    try:
        add_task(title=args.title, due_date=args.due_date)
        print(f"タスク '{args.title}' を追加しました。")
    except Exception as e:
        print(f"エラー: タスクの追加に失敗しました - {e}", file=sys.stderr)
        sys.exit(1)


def handle_list_command(_args):
    """Handle the list command."""
    try:
        tasks = list_tasks()
        if not tasks:
            print("タスクはありません")
            return

        for task in tasks:
            print(f"[{task.id}] {task.title} - {task.due_date}")
    except Exception as e:
        print(f"エラー: タスクの一覧取得に失敗しました - {e}", file=sys.stderr)
        sys.exit(1)


def setup_parser():
    """Set up argument parser with subcommands."""
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add subcommand
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("--title", required=True, help="Task title")
    add_parser.add_argument(
        "--due_date",
        type=parse_date,
        required=False,
        help="Due date in YYYY-MM-DD format",
    )

    # List subcommand
    subparsers.add_parser("list", help="List all tasks")

    return parser


def run_cli():
    """Main CLI entry point."""
    parser = setup_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    command_handlers = {
        "add": handle_add_command,
        "list": handle_list_command,
    }

    handler = command_handlers.get(args.command)
    if handler:
        handler(args)
    else:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        parser.print_help()
        sys.exit(1)
