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

    list_best_product = []

     # Recover db.json
    f = open(db_file_products, 'r')
    db_json = json.load(f)
    for i in range(0,len(db_json["products"])):
        if db_json["products"][i]["id_product"] == id_product:
            list_best_product.append(best_product(db_json["products"][i]["best_product"], db_json["products"][i]))
            product = db_json["products"][i]["product"]
            price = db_json["products"][i]["price"]
            description = db_json["products"][i]["description"]
            stock = db_json["products"][i]["stock"]
            category = db_json["products"][i]["category"]
            return product, price, description, stock, category, list_best_product
    return "The selected product doesn't exist"

def best_product(best_product : bool, db_json):
    if best_product == True:
        return db_json
    else:
        return ""

@app.patch("/product/{id_product}/cart/{id_cart}")
async def add_to_cart(id_product : str, id_cart : str):

    id = check_id_product(id_product)
    cart = check_id_cart(id_cart)
    if id == id_product and cart == id_cart:
        f = open(db_file_carts, "w")
        return f
        # On regarde si le produit existe
        # On regarde si le panier existe
        # On ajoute le produit dans le panier
    else:
        return "The product or the cart doesn't exist"

def check_id_product(id_product):
    f = open(db_file_products, 'r')
    db_json = json.load(f)
    for i in range(0,len(db_json["products"])):
        if id_product == db_json["products"][i]["id_product"]:
            return id_product
    return ""

def check_id_cart(id_cart):
    f = open(db_file_carts, 'r')
    db_json = json.load(f)
    for i in range(0,len(db_json["carts"])):
        return db_json["carts"]
        if id_cart == db_json["carts"][i]["id_cart"]:
            return id_cart
    return ""

