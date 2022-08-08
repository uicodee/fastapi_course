from fastapi import FastAPI
from enum import Enum


app = FastAPI()


class Product(str, Enum):
    carrot = "carrot"
    cucumber = "cucumber"
    apple = "apple"
    orange = "orange"


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def get_me():
    return {"user": "the current user"}


@app.get("/users/{user_id}")
async def get_user(user_id):
    return {"user_id": user_id}


@app.get("/products/{product_name}")
async def get_product(product_name: Product):
    if product_name == Product.carrot:
        return {"product": product_name}
    else:
        return {"product": "this is not carrot ("}


@app.get("/file/{file_path:path}")
async def get_file_path(file_path: str):
    return {"file path": file_path}

