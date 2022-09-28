# Projet_Python
Projet python

# db.json : 

    >> users <<

This is the table of users. 
There is following elements inside :
    - id_user           [STRING]    (ID :  Unique. This is the Nickname and the element of identification.)
    - password          [STRING]    (Obvious, this is a password. No restrictions for it at the moment.)
    - num_buy           [STRING]    (number of element that have been bought by the user. Basicaly used to know who is the best "client").
    - origin            [STRING]    (location of the user, at the creation of his account without any caps) 

    >> commands <<

This is the table of commands. 
There is following elements inside :
    - id_command        [STRING]    (ID: Unique. This start with "COM" and is followed by an incremented number.)
    - id_user           [STRING]    (ID of the client that have passed the command.)
    - content_command   [LIST]      (Here, is the list of element that was in the cart of the user and has been purchased.)

    >> carts <<

This is the table of product that has been put in the cart. 
There is following elements inside :
    - id_cart           [STRING]    (ID : Unique. This start with "CAR" and is followed by an incremented number)
    - id_user           [STRING]    (ID of the client who is passing the command.)
    - content_command   [LIST](That is the content of the command:
                - id_product    [STRING]    (The id of the selected product in the table of existing products)
                - quantity      [INTEGER]   (The number of the product that the client wouldlike to purchase.))

    >> products <<

This is the table of product that exist in our website.
There is following elements inside :
    - product           [STRING]    (A short idication of what is the product)
    - id_product        [STRING]    (ID : Unique. Used to recognize the product in the product table. It start with "PR" and is followed by an incremented number.)
    - description       [STRING]    (This is the complete description of the product. No restriction on the lenght. Originaly used to describe the product.)
    - price             [INT/FLOAT] (Obvious, this is how much the product cost to the customer.)
    - category          [STRING]