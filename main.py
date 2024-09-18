from fastapi import FastAPI, HTTPException, Depends
from schemas import Post
from uuid import UUID
import models
from  datebase import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI(
    title="Blog"
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()


@app.post("/")
def create_post(post: Post, db: Session = Depends(get_db)):
    post_model = models.Post()
    post_model.title = post.title
    post_model.author = post.author
    post_model.text = post.text

    db.add(post_model)
    db.commit()

    return post


@app.put("/{post_id}")
def update_post(post_id: UUID, post: Post):
    count = 0
    for x in POSTS:
        count += 1
        if x.id == post_id:
            POSTS[count - 1] = post
            return POSTS[count - 1]
    raise HTTPException(
        status_code=404,
        detail=f"ID {post_id} не существует",
    )


@app.delete("/{post_id}")
def delete_book(post_id: UUID, post: Post):
    count = 0
    for x in POSTS:
        count += 1
        if x.id == post_id:
            del POSTS[count - 1]
            return f"{post_id} удаен"
    raise HTTPException(
        status_code=404,
        detail=f"ID {post_id} не существует",
    )
