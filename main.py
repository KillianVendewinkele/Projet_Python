from typing_extensions import Required
from fastapi import FastAPI

app = FastAPI()

i_table = ["bite", "cul", "thomas"]

@app.get("/")
async def root():
    return {"message": "Hello, this is the home page"}

@app.get("/yolo")
async def yolo():
    return {"message": "You only live once !"}

@app.get("/thomas")
async def thomas():
    return {"message": hello_bitch('Thomas', 20) }

@app.get("/insult")
async def insult():
    return {"message": i_table }

@app.get("/tuples")
async def tuples():
    return process_items( tuple[1, 3, "bite"])

@app.get("/page/me")
async def pageme():
    return {"message": "All good [200], the current user page"}

@app.get("/page/{item_id}")
async def page(item_id):
    return {"Error 404": "Page " + item_id + " is not found"} 

def hello_bitch(name : str, age: int):
    sentence = "Hello " + name + ", beach of " + str(age) + " years old"
    return sentence

def insults(insult_table : list[str]):
    return insult_table

def process_items(items_t: tuple[int, int, str]):
    return items_t