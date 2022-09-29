from fastapi import FastAPI
import json

app = FastAPI()
# db_file_* is used to set the same db for each function (easy to change)
db_file_users = "users.json"
db_file_commands = "commands.json"
db_file_carts = "carts.json"
db_file_products = "products.json"


# Create the product
@app.post("/products/{id_products}")
async def register(id_products: str):
    if id_products == check_id_products(id_products):
        return "User already taken"
    else:
        return add_products_to_db(db_file_products, id_products)


# Add the user to the json file
def add_products_to_db(file_json: str, id: str, password: str):
    f = open(str(file_json), 'r+')
    db_json = json.load(f)
    db_json["users"].append({
        "id_products": id
    })
    f.close()
    f = open(str(file_json), 'w')
    json.dump(db_json, f, sort_keys=True, indent=4)
    f.close()
    return str(id) + " ok"


# Check the id_user for creating new account
def check_id_products(id_user: str):
    f = open(db_file_users, 'r')
    files = f.read()
    db_json = json.loads(files)
    for i in range(0, len(db_json["products"])):
        if db_json["products"][i]["id_products"] == id_user:
            return db_json["users"][i]["id_products"]
    return "You can create your products"
