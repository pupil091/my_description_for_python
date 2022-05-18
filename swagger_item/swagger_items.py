from typing import List

from fastapi import FastAPI
from pydantic.main import BaseModel


class GetItems(BaseModel):
    id: int
    name: str
    good: bool


class PostAndPutItems(BaseModel):
    id: int
    name: str


app = FastAPI()


@app.get("/get/items/", response_model=GetItems)
def read_status(q: List[str], user_name: GetItems):
    params = {
        "13 monkey": q,
        "Round Dog mf": user_name
    }

    return params


@app.post("/post/items/", response_model=PostAndPutItems)
def check_item(user_name: PostAndPutItems):
    if user_name == '0':
        return "Your code is not available!"
    else:
        return "You have right code."


@app.put("/put/item/{item_name}", response_model=PostAndPutItems)
def reload_item(user_name: PostAndPutItems):
    return user_name


@app.delete("/del/item/{item_name}")
def kick_item(user_name: str):
    return user_name
