from enum import Enum
from typing import Union

from fastapi import FastAPI


class ModelName(str, Enum):
    deathnet = "deathnet"
    whitenet = "whitenet"
    blacknet = "blacknet"


app = FastAPI()


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.deathnet:
        return {"model_name": model_name, "message": "Jump da fuck up mf!"}

    if model_name.value == "blacknet":
        return {"model_name": model_name, "message": "Drugs or alcohol?"}

    return {"model_name": model_name, "message": "Do you have smth for me?"}


@app.put("/users/{user_id}/items/{item_id}")
def read_user_item(
        user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"user_id": user_id, "item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "your words to user(probably)"}
        )
    return item


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/items/{item_id}")
def read_user_item(
        item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

print(sales.items())


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)
