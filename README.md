# FlyRank Backend AI Engineering – BE-04: Containerize Your Stack

This project was developed for the **FlyRank Backend AI Engineering BE-04 – Containerize Your Stack** assignment.

The objective of this assignment is to replace the in-memory repository from the previous service with a PostgreSQL repository, run PostgreSQL inside Docker with persistent storage, and start both the application and database together using Docker Compose.

---

## Assignment Requirements

This project satisfies the assignment requirements by:

- Running PostgreSQL inside Docker.
- Using a Docker volume for persistent database storage.
- Reading the database connection string from a `.env` file.
- Including a `.env.example` file.
- Ignoring `.env` through `.gitignore`.
- Creating the database table using a SQL initialization script.
- Replacing the in-memory repository with a PostgreSQL repository.
- Keeping the service layer and API routes unchanged.
- Starting both the application and PostgreSQL with a single command:

```bash
docker compose up
```

- Demonstrating that data persists after restarting the application and database containers.

---

# Technologies

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- Pydantic

---

# Project Structure

```text
flyrank-be04/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── service.py
│   ├── models.py
│   ├── schemas.py
│   ├── config.py
│   ├── db.py
│   └── repository/
│       ├── base.py
│       ├── memory_repository.py
│       └── postgres_repository.py
│
├── init_db/
│   └── init.sql
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# Repository Architecture

The application follows a repository pattern.

The only change from the previous implementation is the repository.

### Previous

```
InMemoryTaskRepository
```

### Current

```
PostgresTaskRepository
```

The **service layer** and **API routes** remain unchanged.

This demonstrates that changing the storage implementation does not affect the business logic or API endpoints.

---

# Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=tasks_db

DATABASE_URL=postgresql://postgres:postgres@db:5432/tasks_db
```

The `.env` file is ignored by Git.

---

# Running the Project

## Prerequisites

- Docker
- Docker Compose

---

## Start the Application

```bash
docker compose up
```

This command:

- Builds the FastAPI application.
- Starts PostgreSQL.
- Creates the required database table.
- Connects the application to PostgreSQL.
- Exposes the API.

---

## API Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/tasks` | Create a task |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{id}` | Get a task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

---

# Database Initialization

The database schema is created automatically using the SQL initialization script located at:

```text
init_db/init.sql
```

The table is created automatically the first time PostgreSQL starts.

---

# Data Persistence

PostgreSQL stores its data using a Docker volume.

This ensures that application data is preserved even after restarting the application or PostgreSQL container.

---

## Verify Persistence

Start the project:

```bash
docker compose up -d
```

Create a task:

```bash
curl -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Persistence Test","description":"Testing Docker volumes"}'
```

Retrieve tasks:

```bash
curl http://localhost:8000/tasks
```

Restart the application:

```bash
docker compose restart
```

Retrieve tasks again:

```bash
curl http://localhost:8000/tasks
```

If the previously created task is still returned, persistence has been successfully verified.

---

# Stop the Project

Stop containers while keeping the database volume:

```bash
docker compose down
```

Stop containers and remove the database volume:

```bash
docker compose down -v
```

---

# Deliverables

This project includes:

- PostgreSQL running inside Docker
- Docker Compose configuration
- Persistent Docker volume
- SQL initialization script
- PostgreSQL repository implementation
- Environment variable configuration
- `.env.example`
- `.gitignore`
- Complete source code
- Project documentation

---

# Conclusion

This project fulfills the requirements of the **FlyRank Backend AI Engineering BE-04 – Containerize Your Stack** assignment by replacing the in-memory repository with a PostgreSQL implementation, keeping the service layer and routes unchanged, running the complete stack with Docker Compose, and demonstrating persistent data storage across container restarts.

---

# License

MIT License
