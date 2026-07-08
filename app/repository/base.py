from abc import ABC, abstractmethod
from typing import List, Optional

from app.models import Task


class TaskRepository(ABC):
    """Interface implemented by both the in-memory (A2) repository
    and the PostgreSQL repository. The service layer depends only
    on this interface, never on a concrete implementation."""

    @abstractmethod
    def create(self, title: str, description: Optional[str], is_done: bool) -> Task:
        ...

    @abstractmethod
    def get(self, task_id: int) -> Optional[Task]:
        ...

    @abstractmethod
    def list(self) -> List[Task]:
        ...

    @abstractmethod
    def update(self, task_id: int, **fields) -> Optional[Task]:
        ...

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        ...
