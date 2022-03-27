from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


items = [
    {"id": 1, "Name": "item 1 name"},
    {"id": 2, "Name": "item 2 name"},
    {"id": 3, "Name": "item 3 name"},
    {"id": 4, "Name": "item 4 name"},
    {"id": 5, "Name": "item 5 nameee"}
]


@app.get("/items")
def read_root():
    return items


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if((item_id == 0) or (item_id > len(items))):
        return []
    else:
        return items[item_id - 1]
