# Projet_Python
Projet python

# page_product.py : 


    >> product_details(id_product : str) <<

This function recover almost every product details in the json file. It takes one parameter : 

    - id_product  (string) : an unique value for retrieving the product in the json file.

This function returns the product name, the product price, the product description, the product stock, the product category, the list of best product.

    >> best_product(best_product : bool, db_json) <<

This function recover every product that are best product and put them in a list. It takes two parameters : 

    - best_product (boolean) : this value is true if the product is in best_product else this value is not in best_product.
    - db_json (json) : this is the json you want to search for a best product.

This function returns the list of best products if the list exists, else it returns "".

# user.py : 


    >> register(id_user : str, password : str) <<

This function create a user in the json file. It takes two parameters : 

    - id_user (string) : an unique value for retrieving the user in the json file and also the name of the user.
    - password (string) : the password of the user.

This function returns "User already taken" if the id_user already exists in the json file, else it returns the function add_user_to_db() for creating the account.

    >> change_password(id_user : str, password : str) <<

This function update the json file by modifying the password of the selected user to the selected password. It takes two parameters :

    - id_user (string) : an unique value for retrieving the user in the json file and also the name of the selected user.
    - password (string) : the new password for the user.

This function returns "The selected user doesn't exist" if the id_user doesn't exist in the json file, else it returns informations on the selected users after updating the password.

    >> login(id_user : str, password : str) <<

This function check if the user exist in the json file. It takes two parameters :

    - id_user (string) : the selected user id to compare with the user id in the json file.
    - password (string) : the selected password to compare with the password of the user in the json file.

This function returns "You can enter" if the user id and the password exist in the json file, else it returns "Wrong username or password".

    >> add_user_to_db(file_json : str, id : str , password : str) <<

This function add a user in a json file. It takes three parameters :

    - file_json (string) : the json file where you want to add the user.
    - id (string) : the user id to add in the json file.
    - password (string) : the password to add in the json file.

This function returns the string : str(id) + " ok". It shows if the creation of the user is successful or not.

    >> check_id_user(id_user : str) <<

This function check if the id_user already exists in the json file. It takes one parameter : 

    - id_user (string) : the user you want to check with the json file.

This function returns the user id of the json file if it already exists, else it returns the string "You can create your account".
