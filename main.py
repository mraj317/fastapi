from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {
        "title": "title of post 1",
        "content": "content of post 1",
        "id": 1
    },
    {
        "title": "title of post 2",
        "content": "content of post 2",
        "id": 2
    }
]


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post


@app.get("/")
def root():
    return {"message": "World"}

# ALL POSTS


@app.get('/posts')
async def get_posts():
    return {"posts": my_posts}

# CREATE POST


@app.post('/posts')
async def create_post(post: Post):
   # post["id"] = my_posts[-1]["id"] + 1
    print(post.dict())
    my_posts.append(post)
    return {'post': post}

# GET ONE POST


@app.get('/posts/{post_id}')
async def get_post(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    return {"post": post}

# DELETE POST


@app.delete('/posts/{post_id}')
async def delete_post(post_id: int):
    post = find_post(post_id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="post not found")

    my_posts.remove(post)
    return {'post': post}
