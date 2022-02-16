from typing import Optional

from fastapi import FastAPI

from db import get_top_10, get_one_country

app = FastAPI()


@app.get("/")
async def read_root():
    top_10 = get_top_10()
    return top_10


@app.get("/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    one_c = get_one_country(item_id)
    return one_c