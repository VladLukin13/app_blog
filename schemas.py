from pydantic import BaseModel, Field, EmailStr
from typing import Annotated
from uuid import UUID
from datetime import datetime


class Post(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)
    text: str

# class Author(BaseModel):
#     id: UUID
#     username: str
#     email: EmailStr
#     date_of_birth: str
