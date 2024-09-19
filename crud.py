from fastapi import HTTPException, Depends
from schemas import Post
import models
from datebase import get_db
from sqlalchemy.orm import Session


def get_posts(db: Session):
    return db.query(models.Posts).all()


def get_post(post_id_input: int, db: Session):
    return db.query(models.Posts).filter(models.Posts.id == post_id_input).first()


def create_post(post: Post, db: Session):
    post_model = models.Posts()

    post_model.title = post.title
    post_model.author = post.author
    post_model.text = post.text

    db.add(post_model)
    db.commit()

    return post


def update_post(post_id_in: int, post: Post, db: Session):
    post_model = db.query(models.Posts).filter(models.Posts.id == post_id_in).first()

    post_model.title = post.title
    post_model.author = post.author
    post_model.text = post.text

    db.add(post_model)
    db.commit()

    return post


def delete_post(post_id_input: int,  db: Session):
    db.query(models.Posts).filter(models.Posts.id == post_id_input).delete()
    db.commit()
