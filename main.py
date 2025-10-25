from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get('/')
def read_root():
    return('hello world')

@app.get('/items/{item_id}')
def get_item(item_id: str):
    return {"item_id": item_id, "name": "mock"}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return({
        "item_id": item_id,
        "item": {
            "name": item.name,
            "price": item.price, 
            "is_offer": item.is_offer
        } 
        })
