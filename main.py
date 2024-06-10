from fastapi import FastAPI
from core import repo
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.get("/tabs")
def tabs():
    return repo.get_all_tabs()
