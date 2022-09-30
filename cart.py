from posixpath import join
from fastapi import FastAPI
import json

app = FastAPI()
# db_file_* is used to set the same db for each function (easy to change)
db_file_users = "users.json"
db_file_commands = "commands.json"
db_file_carts = "carts.json"
db_file_products = "products.json"

# Check if the cart of the user exist and if yes, it will return the associated cart
@app.get("/carts/{id_user}")
async def display_cart(id_user : str):
    f = open(db_file_carts, 'r')
    files = f.read()
    db_json = json.loads(files)
    for cart in db_json["carts"]:
        if cart["id_user"] == id_user:
            return cart["cart_content"]
    return "There is no cart for this user"

# Check if the cart of the user exist and if yes, it will check if the element exist in the cart and if yes, 1 element will be removed
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