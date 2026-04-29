import argparse
from todo.tasks import add_task, list_tasks, complete_task, remove_task, clear_tasks

def main():
    parser = argparse.ArgumentParser(description="A simple todo CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", help="The task to add")

    subparsers.add_parser("list", help="List all tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task as done or not done")
    done_parser.add_argument("task_id", type=int, help="Task id from the list")

    remove_parser = subparsers.add_parser("remove", help="Remove task from the list")
    remove_parser.add_argument("task_id", type=int, help="Task id from the list")

    subparsers.add_parser("clear", help="Clear all tasks that are done")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        complete_task(args.task_id)
    elif args.command == "remove":
        remove_task(args.task_id)
    elif args.command == "clear":
        clear_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
