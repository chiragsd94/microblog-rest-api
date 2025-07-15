from fastapi import FastAPI
from api.routes.posts import router as PostRouter
from api.routes.comments import router as CommentRouter
from api.db import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(PostRouter)
app.include_router(CommentRouter)
