from posixpath import join
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

# Change password of the specified user
@app.put("/users/{id_user}/{password}")
async def change_password(id_user : str, password : str):

    # Recover db.json
    f = open(db_file_users, 'r')
    db_json = json.load(f)
    f.close()
    f = open(db_file_users, 'w')
    for i in range(0,len(db_json["users"])):
        if db_json["users"][i]["id_user"] == id_user:
            db_json["users"][i]["password"] = password
            json.dump(db_json, f, sort_keys=True, indent = 4)
            f.close()
            return db_json["users"][i]
    f.close()
    return "The selected user doesn't exist"

@app.get("/users/{id_user}/{password}")
async def login(id_user : str, password : str):
    f = open(db_file_users, 'r')
    files = f.read()
    db_json = json.loads(files)
    for i in range(0,len(db_json["users"])):
        if db_json["users"][i]["id_user"] == id_user and db_json["users"][i]["password"] == password:
            return "You can enter"
    return "Wrong username or password"

# Add the user to the json file
def add_user_to_db(file_json : str, id : str , password : str):
    f = open(str(file_json), 'r+')
    db_json = json.load(f)
    db_json["users"].append({
            "id_user":id,
            "password":password
        })
    f.close()
    f = open(str(file_json), 'w')
    json.dump(db_json, f, sort_keys=True, indent = 4)
    f.close()
    return str(id) + " ok"

# Check the id_user for creating new account
def check_id_user(id_user : str):
    
    f = open(db_file_users, 'r')
    files = f.read()
    db_json = json.loads(files)
    for i in range(0,len(db_json["users"])):
        if db_json["users"][i]["id_user"] == id_user:
            return db_json["users"][i]["id_user"]
    return "You can create your account"


# Check if the user exist and if yes, it will return the associated cart
@app.get("/carts/{id_user}")
async def display_cart(id_user : str):
    f = open(db_file_carts, 'r')
    files = f.read()
    db_json = json.loads(files)
    for cart in db_json["carts"]:
        if cart["id_user"] == id_user:
            return cart["cart_content"]
    return "There is no cart for this user"


@app.delete("/carts/{id_user}/delete/{id_product}")
async def delete_product(id_user : str, id_product : str):
    f = open(db_file_carts, 'r+')
    files = f.read()
    db_json = json.loads(files)
    f.close()
    for i in range(0, len(db_json["carts"])):
        if db_json["carts"][i]["id_user"] == id_user:
            for j in range(0, len(db_json["carts"][i])):
                if db_json["carts"][i]["cart_content"][j]["id_products"] == id_product:
                    if db_json["carts"][i]["cart_content"][j]["quantity"] <= 1:
                        db_json["carts"][i]["cart_content"].pop(j) #"product " + id_product + " deleted"
                    else:
                        db_json["carts"][i]["cart_content"][j]["quantity"] = int(db_json["carts"][i]["cart_content"][j]["quantity"]) -1
                    g = open(str(db_file_carts), 'w')
                    json.dump(db_json, g, sort_keys=True, indent = 4)
                    f.close()
                    return 200
    return 404