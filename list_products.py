from fastapi import FastAPI
import json

app = FastAPI()
# db_file_* is used to set the same db for each function (easy to change)
db_file_users = "users.json"
db_file_commands = "commands.json"
db_file_carts = "carts.json"
db_file_products = "products.json"


@app.get("/products")
async def read_products(category: str, description: str, id_product: str, price: str, product: str, stock: str):
    f = open(db_file_products, 'r')
    files = f.read()
    db_json = json.loads(files)
    return {"category": category, "description": description, "id_product": id_product, "price": price,
            "product": product, "stock": stock}
