from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="FlyRank BE-04 - Containerized Task Service")

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
