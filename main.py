from fastapi import FastAPI, Depends
from models.todo import Todo
from sqlalchemy.orm import Session
from utils.database import get_db
import uvicorn

app = FastAPI(title="Simple to do list", version="1.0.0")


@app.get("/")
def root():
    return {"Message": "Hello World"}

@app.get("/todos")
def get_tasks(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos

@app.post("/todos/")
def create_task(task_name: str, is_completed: bool, db: Session=Depends(get_db)):
    task = Todo(task_name=task_name, is_completed= is_completed)
    db.add(task)
    db.commit()
    db.refresh(task)
    return {"task": task}

@app.put("/todos/")
def update_task(task_id: int, is_completed: bool, db: Session=Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task:
        task.is_completed = not task.is_completed
        db.commit()
        db.refresh(task)
        return {"task": task}
    return {"error": "Task not found"}

@app.patch("/todos/")
def patch_task(task_id: int, task_name: str, db: Session=Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task:
        task.task_name = task_name
        db.commit()
        db.refresh(task)
        return {"task": task}
    return {"error": "Task not found"}

@app.delete("/todos/")
def delete_task(task_id: int, db: Session=Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Task deleted"}
    return {"error": "Task not found"}


    

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
