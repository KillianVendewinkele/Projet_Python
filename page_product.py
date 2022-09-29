from unicodedata import category
from fastapi import FastAPI
import json

app = FastAPI()
# db_file_* is used to set the same db for each function (easy to change)
db_file_users = "users.json"
db_file_commands = "commands.json"
db_file_carts = "carts.json"
db_file_products = "products.json"

# Get the product name, price and description
@app.get("/product/{id_product}")
async def product_details(id_product : str):

     # Recover db.json
    f = open(db_file_products, 'r')
    db_json = json.load(f)
    for i in range(0,len(db_json["products"])):
        if db_json["products"][i]["id_product"] == id_product:
            product = db_json["products"][i]["product"]
            price = db_json["products"][i]["price"]
            description = db_json["products"][i]["description"]
            stock = db_json["products"][i]["stock"]
            category = db_json["products"][i]["category"]
            return product, price, description, stock, category
    return "The selected product doesn't exist"
