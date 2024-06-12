from fastapi import FastAPI
from core import repo, cache
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.get("/tabs")
def get_tabs():
    return repo.get_all_tabs()


@app.get("/cache")
def get_cache(tab: int):
    return cache.get_cached(tab)
