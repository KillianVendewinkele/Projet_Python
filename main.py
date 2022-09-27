from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():

    return {"message": "Hello world"}

@app.get("/name")
async def name():
    return get_name_with_age(test_get_name("kpjc", "jzvoijz"), 22)

def get_name_with_age(name : str, age : int):
    name_with_age = name + " is this old : " + str(age)
    return name_with_age

def test_get_name(first_name : str, last_name : str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name




























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