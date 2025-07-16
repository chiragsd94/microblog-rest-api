from fastapi import FastAPI
from sqlalchemy import create_engine
from api.db import database, metadata
from api.config import settings

from api.routes.posts import router as PostRouter
from api.routes.comments import router as CommentRouter

from api.models import Post, Comment

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

app = FastAPI()


@app.on_event("startup")
async def startup():
    metadata.create_all(engine)
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(PostRouter)
app.include_router(CommentRouter)
