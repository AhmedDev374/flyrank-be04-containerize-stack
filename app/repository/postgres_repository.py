from typing import List, Optional

import psycopg2.extras

from app.db import get_connection
from app.models import Task
from app.repository.base import TaskRepository


class PostgresTaskRepository(TaskRepository):
    """PostgreSQL-backed implementation of TaskRepository.
    It implements the exact same interface as InMemoryTaskRepository,
    so the service layer and API routes work unchanged."""

    def create(self, title: str, description: Optional[str], is_done: bool) -> Task:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(
                    """
                    INSERT INTO tasks (title, description, is_done)
                    VALUES (%s, %s, %s)
                    RETURNING id, title, description, is_done, created_at;
                    """,
                    (title, description, is_done),
                )
                row = cur.fetchone()
                return Task(**row)

    def get(self, task_id: int) -> Optional[Task]:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(
                    "SELECT id, title, description, is_done, created_at "
                    "FROM tasks WHERE id = %s;",
                    (task_id,),
                )
                row = cur.fetchone()
                return Task(**row) if row else None

    def list(self) -> List[Task]:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(
                    "SELECT id, title, description, is_done, created_at "
                    "FROM tasks ORDER BY id;"
                )
                rows = cur.fetchall()
                return [Task(**row) for row in rows]

    def update(self, task_id: int, **fields) -> Optional[Task]:
        updates = {k: v for k, v in fields.items() if v is not None}
        if not updates:
            return self.get(task_id)

        set_clause = ", ".join(f"{column} = %s" for column in updates)
        values = list(updates.values()) + [task_id]

        with get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(
                    f"UPDATE tasks SET {set_clause} WHERE id = %s "
                    f"RETURNING id, title, description, is_done, created_at;",
                    values,
                )
                row = cur.fetchone()
                return Task(**row) if row else None

    def delete(self, task_id: int) -> bool:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
                return cur.rowcount > 0
