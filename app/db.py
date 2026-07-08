from contextlib import contextmanager

import psycopg2

from app.config import DATABASE_URL


@contextmanager
def get_connection():
    """Yields a PostgreSQL connection, committing on success and
    rolling back on error. Used only by the PostgreSQL repository."""
    conn = psycopg2.connect(DATABASE_URL)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
