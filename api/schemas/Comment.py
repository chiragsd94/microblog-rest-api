from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional, List


class BaseComment(BaseModel):
    body: str
    created: datetime = Field(default_factory=datetime.utcnow)


class Comment(BaseComment):
    id: int
    post_id: int
