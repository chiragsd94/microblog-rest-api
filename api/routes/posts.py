from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/posts",
    tags=["Posts"],
)


@router.get("/")
async def get_all_posts():
    return {"message": "All posts"}


@router.post("/")
async def create_post():
    return {"message": "Create post"}


@router.get("/{id}")
async def get_post(id: int):
    return {"message": f"Post with ID {id}"}


@router.put("/{id}")
async def update_post(id: int):
    return {"message": f"Updated post with ID {id}"}


@router.delete("/{id}")
async def delete_post(id: int):
    return {"message": f"Deleted post with ID {id}"}
