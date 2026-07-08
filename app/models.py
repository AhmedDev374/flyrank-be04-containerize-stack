from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    """Domain model. Both the in-memory and PostgreSQL repositories
    return/consume this same model, so the service layer and API
    routes never need to know which repository is backing them."""

    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    is_done: bool = False
    created_at: Optional[datetime] = None
