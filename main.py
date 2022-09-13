from enum import Enum
from typing import Union
from fastapi import FastAPI


class MlModel(str, Enum):
    value1 = "value1"
    value2 = "value2"
    value3 = "value3"

fake_db_items = [{"item_name": "glass"}, {"item_name": "headphone"}, {"item_name": "laptop"}]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/item_id')
async def read_paramteres(item_id: str, q: Union[str, None] = None, short: bool = False):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id, "short": short}


@app.get('/items/')
async def read_items(skip: int = 0, limit: int = 10):
    return fake_db_items[skip:skip+limit]


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"message": item_id}


@app.get('/user/me')
async def current_user():
    return { "message": "the current user"}


@app.get('/user/{user_name}')
async def read_user(user_name: str):
    return { "message": user_name}


@app.get('/models/{models_name}')
async def read_model(models_name: MlModel):
    return { "model": models_name, "data": MlModel.value1}

@app.get('/file/{file_path:path}')
async def read_path(file_path):
    return { "path": file_path}