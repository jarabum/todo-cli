# todo-cli

A simple command-line todo list that works anywhere on your system.

## Installation

Make sure you have [pipx](https://pipx.pypa.io) installed, then run inside the project folder:

```bash
pipx install .
```

## Usage

```bash
todo add "buy milk"       # add a task
todo list                 # list all tasks
todo done 1               # mark task 1 as done
todo done 1               # mark task 1 as not done
todo remove 1             # delete task 1
```

## Example

```
$ todo add "buy milk"
Added task: buy milk

$ todo add "walk the dog"
Added task: walk the dog

$ todo list
1. ○ buy milk
2. ○ walk the dog

$ todo done 1
Task: 'buy milk' marked as done

$ todo list
1. ✓ buy milk
2. ○ walk the dog
```

## Development

Clone the repo and install in editable mode:

```bash
git clone https://github.com/yourusername/todo-cli
cd todo-cli
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Tasks are saved to `~/.todo_tasks.json`.
