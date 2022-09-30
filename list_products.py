from fastapi import FastAPI
import json

app = FastAPI()
# db_file_* is used to set the same db for each function (easy to change)
db_file_users = "users.json"
db_file_commands = "commands.json"
db_file_carts = "carts.json"
db_file_products = "products.json"


@app.get("/products")
async def read_list_products(limit: int):
    f = open(db_file_products, 'r')
    files = f.read()
    db_json_out = {}
    db_json = json.loads(files)
    for i in range(1, limit +1):
        db_json_out[i] = db_json["products"][i-1]
    return db_json_out


@app.get("/products/{category}")
async def read_products(category: str):
    # Recover db.json
    f = open(db_file_products, 'r')
    files = f.read()
    db_json = json.loads(files)
    list_product = []
    for i in range(0, len(db_json["products"])):
        if db_json["products"][i]["category"] == category:
            list_product.append(db_json["products"][i])
    if list_product != []:
        return list_product
    return "The selected category doesn't exist"

# @app.get("/products/list")
# async def read_products():
# product_list = list(db_file_products)
# return product_list
