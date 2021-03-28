from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# temp database
mangadb = []

# manga model to store mangas
class Manga(BaseModel):
    id: int
    name: str
    price: float

# Home/welcome route
@app.get("/")
def read_root():
    return {"greetings": "Welcome to Mangastore!!!"}

# Get all Mangas
@app.get("/mangas")
def get_mangas():
    return mangadb

# get single manga
@app.get("/mangas/{manga_id}")
def get_a_manga(manga_id: int):
    manga = manga_id - 1
    return mangadb[manga]

# add a new manga
@app.post("/mangas")
def add_manga(manga: Manga):
    mangadb.append(manga.dict())
    return mangadb[-1]

# delete a manga
@app.delete("/mangas/{manga_id}")
def delete_manga(manga_id: int):
    mangadb.pop(manga_id-1)
    return {"task": "deletion successful"}
