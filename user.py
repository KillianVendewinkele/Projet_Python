import json
from fastapi import FastAPI
import json

app = FastAPI()

# Check the id_user for creating new account
@app.get("/users")
async def check_id_user(id_user : str):

    # Recover db.json
    with open('db.json') as file:
        db_json = json.loads(file)
    
    for i in range(db_json.users):
        if db_json.users.id_user[i] == id_user:
            return {db_json.users[i].id_user}
        else:
            return id_user

# Create the user
@app.post("/users/{id_user}/{password}")
async def register(id_user : str, password : str):
        if id_user == check_id_user(id_user):
            return "User already taken"
        else:
            return {"id_user" : id_user, "password" : password}

# Change password
@app.patch("users/{id_user}/{password}")
async def change_password(id_user : str, password : str):
    file = open('db.json', 'w')
    db_json = json.loads(file)
    return db_json
    for i in range(db_json.users):
        if db_json.users[i].id_user == id_user:
            file.write()

    db_json.users.password = password