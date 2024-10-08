from fastapi import FastAPI
from enum import Enum
from typing import Optional
app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, Workldjh!"}
@app.post("/")
async def post():
    return {"message": "hello from the post route"}


# @app.get("/items")
# async def list_items():
#     return {"message": "list items route"}


@app.get("/items/{item_id}")
async def list_items(item_id: int):
    return {"item_id": item_id}

class FoodEnum(str, Enum):
    fruits = "Fruits"
    vegetables = "vegetables"
    dairy = "Dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {
            "food_name": food_name, 
            "message": "You have selected vegetables"
            }
    elif food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message": "You have selected fruits"
        }
    else:
        return {
            "food_name": food_name,
            "message": "You have selected dairy"
        }
    
fake_items_db = [{"item_name": "food"},{"item_name": "pot"},{"item_name": "box"}]

@app.get("/items")
async def list_items(skip: int = 0, limit: int =10):
    return fake_items_db[skip : skip +limit]


@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Optional[str]= None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}