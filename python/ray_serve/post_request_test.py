from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

class FaceData(BaseModel):
    label: str | None = None
    vals: List[float]
    # name: str
    # price: float
    # tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: FaceData):
    return item