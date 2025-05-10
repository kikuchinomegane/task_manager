from pydantic import BaseModel
from datetime import date


class Task(BaseModel):
    id: int
    title: str
    due_date: date
