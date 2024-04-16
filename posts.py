
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()


# Recurso
class Post(BaseModel):
    id: int
    likes: int
    comments: List[str] = None
    user: str


# Data guardada en memoria
posts = [Post(id=123, likes=123, comments=["ola", "wasa"], user="owo"),
         Post(id=50, likes=324, comments=["chao", "uwu"], user="owo")]


@app.get("/")
def hello():
    return "Hello World from my API"


@app.get("/posts")
def get_posts(id: int | None = None):
    print(id)
    if id is not None:
        for post in posts:
            if post.id == id:
                return post

        raise HTTPException(status_code=404, detail="Post not found")
    return posts


@app.get("/posts/{id}")  # PATH PARAMETER
def get_post(id: int):
    print(type(id))
    for post in posts:
        if post.id == id:
            return post
    return "post no encontrado"

@app.get("/postsq")
def get_post_query(id: int):
    for post in posts:
        if post.id == id:
            return post
    return "post no encontrado"

@app.post("/posts")
def create_posts(post: Post):
    posts.append(post)
    return post
