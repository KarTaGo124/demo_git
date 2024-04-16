from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Union

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    stock: bool = True


items = []


@app.get("/")
def hello():
    return "Hello World from my API (get)"


@app.post("/")
def hello():
    return "Hello World from my API (post)"


@app.post("/items")
def add_item(item: Item, response: Response):
    response.status_code = 201
    items.append(item)
    return {"item": item}



@app.get("/items")  # QUERY PARAMETER (las dos funciones en una porque tienen la misma ruta)
def get_item_by_ID(response: Response, id: Union[int, None] = None):
    if id is None:
        return {"items": items}
    for item in items:
        if item.id == id:
            return {"item": item}
    response.status_code = 404
    return "Item no encontrado"


