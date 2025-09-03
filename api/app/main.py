from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI()

# MongoDB connection
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://mongodb:27017")
client = MongoClient(MONGODB_URL)
db = client["classified"]
collection = db["users"]

# Pydantic model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with MongoDB UPDATED!"}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    result = collection.insert_one(item_dict)
    return {"id": str(result.inserted_id), **item_dict}

@app.get("/items/")
async def read_items():
    items = list(collection.find())
    for item in items:
        item["_id"] = str(item["_id"])
    return {"items": items}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    from bson import ObjectId
    try:
        item = collection.find_one({"_id": ObjectId(item_id)})
        if item:
            item["_id"] = str(item["_id"])
            return item
        raise HTTPException(status_code=404, detail="Item not found")
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")
