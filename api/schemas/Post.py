from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional, List
from api.schemas.Comment import Comment


class BasePost(BaseModel):
    body: str
    created: datetime = Field(default_factory=datetime.utcnow)
    updated: datetime = Field(default_factory=datetime.utcnow)


class Post(BasePost):
    id: int
    comments: Optional[List[Comment]] = []


class PostUpdate(BaseModel):
    id: int
    body: Optional[str]
