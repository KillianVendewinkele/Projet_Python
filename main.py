from enum import Enum
from fastapi import FastAPI

app = FastAPI()

i_table = ["Aie", "bobo", "thomas"]

@app.get("/")
async def root():
    return {"message": "Hello, this is the home page"}

@app.get("/yolo")
async def yolo():
    return {"message": "You only live once !"}

@app.get("/thomas")
async def thomas():
    return {"message": hello_sir('Thomas', 20) }

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

def hello_sir(name : str, age: int):
    sentence = "Hello " + name + ", pe of " + str(age) + " years old"
    return sentence

def insults(insult_table : list[str]):
    return insult_table

def process_items(items_t: tuple[int, int, str]):
    return items_t

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/skiplimits/")
async def skiplimits(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]