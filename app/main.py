from fastapi import FastAPI
from app.database.connection import engine, Base
from app.models import task_model
from app.routes.task_routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Task Manager API is running"}