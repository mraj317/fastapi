from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "With Love from FastAPI!"}
