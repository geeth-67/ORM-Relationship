from fastapi import FastAPI

from teacher_routes import router as teacher_router

app = FastAPI(
    title="Teacher",
)
