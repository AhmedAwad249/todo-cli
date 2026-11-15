import json, sys, os

FILE = os.environ.get("TODO_FILE", "tasks.json")


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)


def save(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add(text):
    tasks = load()
    tasks.append({"text": text, "done": False})
    save(tasks)


def done(n):
    tasks = load()
    if not 1 <= n <= len(tasks):
        sys.exit(f"no task {n}")
    tasks[n - 1]["done"] = True
    save(tasks)


def list_tasks():
    for i, t in enumerate(load(), 1):
        print(f"{i}. [{'x' if t['done'] else ' '}] {t['text']}")


def main(argv):
    if len(argv) >= 3 and argv[1] == "add":
        add(" ".join(argv[2:]))
    elif len(argv) == 2 and argv[1] == "list":
        list_tasks()
    elif len(argv) == 3 and argv[1] == "done" and argv[2].isdigit():
        done(int(argv[2]))
    else:
        print("usage: todo.py add <text> | list | done <n>")


if __name__ == "__main__":
    main(sys.argv)
