import os

from dotenv import load_dotenv

# Load variables from a local .env file (used for local/dev runs;
# in Docker Compose the values are injected via env_file instead).
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://flyrank:flyrank_password@localhost:5432/flyrank_db",
)
