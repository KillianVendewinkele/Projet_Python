from fastapi import FastAPI
import json

app = FastAPI()
# db_file_* is used to set the same db for each function (easy to change)
db_file_users = "users.json"
db_file_commands = "commands.json"
db_file_carts = "carts.json"
db_file_products = "products.json"

# Create the user
@app.post("/users/{id_user}/{password}")
async def register(id_user : str, password : str):
        if id_user == check_id_user(id_user):
            return "User already taken"
        else:
            return add_user_to_db(db_file_users, id_user, password)

def add_user_to_db(file_json : str, id : str , password : str):
    f = open(str(file_json), 'r+')
    db_json = json.load(f)
    db_json["users"].append({
            "id_user":id,
            "password":password
        })
    f.close()
    f = open(str(file_json), 'w')
    json.dump(db_json, f, sort_keys=True, indent=4)
    f.close()
    return str(id) + "ok"

# Change password
@app.patch("users/{id_user}/{password}")
async def change_password(id_user : str, password : str):
    file = open(db_file_users, 'w')
    db_json = json.loads(file)
    return db_json
    for i in range(db_json.users):
        if db_json.users[i].id_user == id_user:
            file.write()

    db_json.users.password = password



# Check the id_user for creating new account
def check_id_user(id_user : str):
    
    # Recover db.json
    f = open(db_file_users, 'r')
    files = f.read()
    db_json = json.loads(files)
    for i in range(0,len(db_json["users"])):
        if db_json["users"][i]["id_user"] == id_user:
            return db_json["users"][i]["id_user"]
        else:
            print(0)
    return "You can create your account"