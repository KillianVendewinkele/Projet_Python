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
    product = ""

     # Recover db.json
    f = open(db_file_products, 'r')
    db_json = json.load(f)

    for i in range(0,len(db_json["products"])):
        list_best_product.append(best_product(db_json["products"][i]["best_product"], db_json["products"][i]))
        if db_json["products"][i]["id_product"] == id_product:
            product = db_json["products"][i]["product"]
            price = db_json["products"][i]["price"]
            description = db_json["products"][i]["description"]
            stock = db_json["products"][i]["stock"]
            category = db_json["products"][i]["category"]
    if product != "":
        return product, price, description, stock, category, list_best_product
    return "The selected product doesn't exist"

@app.post("/cart/{id_user}/product/{id_product}")
async def add_to_cart(id_user : str, id_product : str):
    product_found = ""
    f = open(db_file_carts, 'r')
    f_file = f.read()
    db_json = json.load(f_file)
    f_file.close()
    g = open(db_file_products, 'r+')
    g_file = g.read()
    db_json2 = json.load(g_file)
    g_file.close()
    for i in range(0,len(db_json["carts"])):
        if db_json["carts"][i]["id_user"] == id_user: # if the user already have a cart
            pass
        else : # if the user doesn't already have a cart
            # create a cart for the user
            print("bite")
        # check for each products in the cart if he already exist
        for k in range(0, len(db_json["carts"][i]["cart_content"])): 
            if str(id_product) == db_json["carts"][i]["cart_content"][k]["id_products"]:
                product_found = "cart"
        # check for each products if he exist in products database
        for j in range(0, len(db_json2["products"])):
            if product_found: break    
            if (str(id_product) == db_json2["products"][j]["id_product"]):
                product_found = "product"
        # if the product exist in the cart:
        if product_found == "cart": 
            for j in range(0, len(db_json["carts"][i])):
                if db_json["carts"][i]["cart_content"][j]["id_products"] == id_product:
                    db_json["carts"][i]["cart_content"][j]["quantity"] += 1
                    break
        # if the product exist in the products database (but not in the cart)
        elif product_found == "product":
            for j in range(0, len(db_json["carts"][i])):
                if db_json["carts"][i]["cart_content"][j]["id_products"] == id_product:
                    db_json["carts"][i]["cart_content"][j]["quantity"] = 1
                    break
        else:
            return 404
        
    h = open(str(db_file_carts), 'w')
    json.dump(db_json, h, sort_keys=True, indent = 4)
    h.close()
        

    # Recover the right cart for 
    # if id_user = user :
    #   Recover the right product for 
    #       If stock > 0 & cart[element] number < stock
    #           If quantity > 0 
    #               add 1 to the quantity in the cart (of the selected product <- user)
    #           else
    #           create a new product in cart_content
    #       Else
    #           return 404

    

def best_product(best_product : bool, db_json):

    if best_product == True:
        return db_json
    else:
        return 404

