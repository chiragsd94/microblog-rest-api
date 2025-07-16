from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from api.db import metadata


post_table = Table(
    "comments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("body", String, nullable=False),
    Column("created", DateTime, default=datetime.utcnow),
    Column("updated", DateTime, default=datetime.utcnow),
    Column("post_id", ForeignKey("posts.id"), nullable=False),
)
