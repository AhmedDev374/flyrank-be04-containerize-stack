from typing import List, Optional

from app.models import Task
from app.repository.base import TaskRepository


class TaskService:
    """Unchanged from the A2 assignment. It only talks to the
    TaskRepository interface, so it has no idea whether it is
    backed by memory or PostgreSQL."""

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, title: str, description: Optional[str], is_done: bool) -> Task:
        return self.repository.create(title=title, description=description, is_done=is_done)

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.repository.get(task_id)

    def list_tasks(self) -> List[Task]:
        return self.repository.list()

    def update_task(self, task_id: int, **fields) -> Optional[Task]:
        return self.repository.update(task_id, **fields)

    def delete_task(self, task_id: int) -> bool:
        return self.repository.delete(task_id)
