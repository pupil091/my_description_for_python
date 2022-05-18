from typing import List
from typing import Optional

from fastapi import FastAPI
from pydantic.main import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


@app.get('/')
def read_root():
    return {'JUMPDAFUCKUP': 'THE WHOLE WORLD'}


@app.get('/things/{thing_id}')
def read_thing(thing_id: int, q: Optional[str] = None):
    return {'thing_id': thing_id, 'q': q}


@app.post('/cock/top/socket')
def change_cock(cock: Item):
    return cock
