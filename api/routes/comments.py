from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/posts",
    tags=["Comments"],
)


@router.post("/{post_id}/comments")
async def create_comment(post_id: int):
    return {"message": f"Created comment on post {post_id}"}


@router.get("/{post_id}/comments/{comment_id}")
async def get_comment(post_id: int, comment_id: int):
    return {"message": f"Post {post_id}, Comment {comment_id}"}
