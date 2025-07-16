from fastapi import APIRouter
from api.schemas.Post import PostInput, PostOutPut
from api.models.Post import post_table
from datetime import date, datetime
from api.db import database


router = APIRouter(
    prefix="/api/v1/posts",
    tags=["Posts"],
)


@router.get("/")
async def get_all_posts():
    return {"message": "All posts"}


@router.post("/")
async def create_post(request: PostInput):
    data = request.model_dump()
    query = post_table.insert().values(body=data["body"])
    await database.execute(query)

    return {"message": "post created"}


@router.get("/{id}")
async def get_post(id: int):
    return {"message": f"Post with ID {id}"}


@router.put("/{id}")
async def update_post(id: int):
    return {"message": f"Updated post with ID {id}"}


@router.delete("/{id}")
async def delete_post(id: int):
    return {"message": f"Deleted post with ID {id}"}
