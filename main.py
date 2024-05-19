from fastapi import FastAPI
from core import repo

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.get("/tabs")
def tabs():
    return repo.get_all_tabs()
