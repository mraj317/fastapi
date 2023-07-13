from fastapi import FastAPI

app = FastAPI()

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


@app.get("/")
def root():
    return {"message": "World"}


@app.get('/posts')
async def get_posts():
    return {"posts": my_posts}
