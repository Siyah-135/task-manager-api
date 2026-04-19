from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: str
    status: str