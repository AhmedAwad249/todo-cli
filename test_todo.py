import os, tempfile
os.environ["TODO_FILE"] = os.path.join(tempfile.mkdtemp(), "t.json")
import todo

todo.add("a"); todo.add("b")
todo.done(2)
assert todo.load() == [{"text": "a", "done": False}, {"text": "b", "done": True}]
print("ok")
