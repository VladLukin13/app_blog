from fastapi import FastAPI, HTTPException, Depends
from schemas import Post
import models
import crud
from datebase import engine, SessionLocal, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog"
)


@app.get("/")
def get_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)


@app.post("/")
def create_post(post: Post, db: Session = Depends(get_db)):
    return crud.create_post(post, db)


@app.put("/{post_id}")
def update_post(post_id: int, post: Post, db: Session = Depends(get_db)):
    post_model = crud.update_post(post_id_in=post_id, post=post, db=db)

    if post_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {post_id} не существует",
        )

    return post_model


@app.delete("/{post_id}")
def delete_post(post_id: int, post: Post, db: Session = Depends(get_db)):
    model_post = crud.get_post(post_id_input=post_id, db=db)
    if model_post is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {post_id} не существует",
        )
    crud.delete_post(post_id_input=post_id, db=db)
