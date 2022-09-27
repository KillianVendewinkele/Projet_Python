from fastapi import FastAPI
from typing import Tuple, Union, Optional

app = FastAPI()


@app.get("/")
async def root():

    return {"message": "Hello world"}

@app.get("/name")
async def name():
    return name_with_age(test_name("kpjc", "jzvoijz"), 22)

@app.get("/type")
async def type():
    return process_items(["A", "B", "C"])

def name_with_age(name : str, age : int):
    name_with_age = name + " is this old : " + str(age)
    return name_with_age

def test_name(first_name : str, last_name : str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def process_items(items : list[str]):
    for item in items:
        print(item)

def process_item(items_t : Tuple[int, int, str]):
    return items_t

def process_item2(item : Union[int, str]):
    return item

def process_items2(items : Optional[str] = None):
    if items is not None:
        return "Hello " + items
    else:
        return "Hello World"






























#
#                    _________________
#                   / /''''''/ /''''\ \
#         _________/ /______/ /______\ \_______
#        /_|                                 |_\
#_______/ _____                         _____  |___________________________________________________________________________________________
#       |// --\\_______________________// --\\_/
# ____    \- -/  _____            _____ \- -/       _____               _____               _____               ____                ____
#
#__________________________________________________________________________________________________________________________________________