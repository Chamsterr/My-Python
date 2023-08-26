from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class TodoItem(BaseModel):
    id: int
    title: str
    description: str
    status: bool

todos: list[TodoItem] = [
    TodoItem(id=0, title="Помыть кота", description="Песецких", status=False)
]

@app.post("/create_new_todo")
def create_new_todo(todo_item: TodoItem):
    todos.append(todo_item)
    return {"status": 200}

@app.get("/get_all_tasks")
def get_all_tasks() -> list[TodoItem]:
    return todos

@app.get("/get_task_by_id/{id}")
def get_task_by_id(id: int) -> TodoItem:
    return next(task for task in todos if task.id == id)

@app.patch("/update_status_task_by_id/{id}")
def update_status_task_by_id(id: int):
    task = next(task for task in todos if task.id == id)
    task.status = not task.status

@app.patch("/delete_task_by_id/{id}")
def delete_task_by_id(id: int):
    task = next(task for task in todos if task.id == id)
    todos.remove(task)