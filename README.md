# todo-cli

A simple command-line todo list that works anywhere on your system.

## Installation

Clone the repository and install with [pipx](https://pipx.pypa.io) inside the project folder:

```bash
git clone https://github.com/jarabum/todo-cli.git
cd todo-cli
pipx install .
```

## Usage

```bash
todo add "buy milk" --priority low       # add a task with priority set to low
todo list                                # list all tasks
todo done 1                              # mark task 1 as done
todo done 1                              # mark task 1 as not done
todo remove 1                            # delete task 1
todo clear                               # remove all done tasks
```

## Example

```
$ todo add "buy milk"
Added task: buy milk

$ todo add "walk the dog"
Added task: walk the dog

$ todo list
1. [ ] buy milk
2. [ ] walk the dog

$ todo done 1
Task: buy milk marked as done

$ todo list
1. [x] buy milk
2. [ ] walk the dog
```

## Development

Clone the repo and install in editable mode:

```bash
git clone https://github.com/jarabum/todo-cli.git
cd todo-cli
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Tasks are saved to `~/.todo_tasks.json`.
