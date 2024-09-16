from fastapi import FastAPI, HTTPException
from schemas import Post
from uuid import UUID

app = FastAPI(
    title="Blog"
)

POSTS = []


@app.get("/")
def get_posts():
    return POSTS


@app.post("/")
def create_post(post: Post):
    POSTS.append(post)
    return post


@app.put("/{post_id}")
def update_post(post_id: UUID, post: Post):
    counter = 0

    for x in POSTS:
        counter += 1
        if x.id == post_id:
            POSTS[counter - 1] = post
            return POSTS[counter - 1]
    raise HTTPException(
        status_code=404,
        detail=f"ID {post_id} не существует",
    )
