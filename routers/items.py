from fastapi import APIRouter
from models.item import Task, TaskOut

router = APIRouter(prefix="/tasks", tags=["tasks"])

tasks_db = []

@router.get("/")
def get_tasks():
    return tasks_db

@router.post("/", response_model=TaskOut)
def create_task(item: Task):
    tasks_db.append(item)
    return item

@router.get("/{task_id}", response_model=TaskOut)
def get_task_by_id(task_id: int):
    for item in tasks_db:
        if item.id == task_id:
            return item