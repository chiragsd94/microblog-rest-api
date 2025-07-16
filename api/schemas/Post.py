from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional, List
from api.schemas.Comment import Comment


class PostInput(BaseModel):
    body: str


class PostOutPut(BaseModel):
    id: int
    body: str
    created_at: datetime
    updated_at: datetime
    comments: Optional[List[Comment]] = []


class PostUpdate(BaseModel):
    id: int
    body: Optional[str]
