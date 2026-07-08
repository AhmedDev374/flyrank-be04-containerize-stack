from datetime import datetime
from itertools import count
from typing import Dict, List, Optional

from app.models import Task
from app.repository.base import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    """This is the original A2 repository. It is kept in the codebase
    unchanged to show that the PostgreSQL repository implements the
    exact same interface (TaskRepository) and could be swapped back
    in at any time without touching the service layer or the routes."""

    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._id_counter = count(1)

    def create(self, title: str, description: Optional[str], is_done: bool) -> Task:
        task_id = next(self._id_counter)
        task = Task(
            id=task_id,
            title=title,
            description=description,
            is_done=is_done,
            created_at=datetime.utcnow(),
        )
        self._tasks[task_id] = task
        return task

    def get(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def list(self) -> List[Task]:
        return list(self._tasks.values())

    def update(self, task_id: int, **fields) -> Optional[Task]:
        task = self._tasks.get(task_id)
        if not task:
            return None
        updates = {k: v for k, v in fields.items() if v is not None}
        updated = task.copy(update=updates)
        self._tasks[task_id] = updated
        return updated

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None
