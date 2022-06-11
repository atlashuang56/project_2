# FastApi sample code .... 2022.06.10
# run it: "uvicorn main:app --reload", Ctrl+Z to stop

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test/")
def read_root():
    return ("here is path /test/ ","the second string")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
