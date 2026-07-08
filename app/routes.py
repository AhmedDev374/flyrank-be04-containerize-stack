from typing import List

from fastapi import APIRouter, HTTPException

from app.models import Task
from app.repository.postgres_repository import PostgresTaskRepository
from app.schemas import TaskCreate, TaskUpdate
from app.service import TaskService

router = APIRouter()

# This is the ONLY line that changed compared to A2:
# repository = InMemoryTaskRepository()  -->  repository = PostgresTaskRepository()
repository = PostgresTaskRepository()
service = TaskService(repository)


@router.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    return service.create_task(payload.title, payload.description, payload.is_done)


@router.get("/tasks", response_model=List[Task])
def list_tasks():
    return service.list_tasks()


@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate):
    task = service.update_task(task_id, **payload.dict())
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    deleted = service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
