import gridfs
import os
from pymongo import MongoClient
from datetime import time
import datetime
import time

product_client = MongoClient(
    'mongodb+srv://qopinstore:%211Supremebot@qop-bot-xe3ad.mongodb.net/test?retryWrites=true&w=majority')
database = product_client["Product-DB"]
user_collection = database["User-Info-Collection"]

def login(user_name, password):
    return

def alreadyExists(newID):
    exists = user_collection.find({'_id': {'$in': newID}})
    return exists

def sign_up():
    print("Make a Username and Password...")
    exists = True
    while exists:
        username = input("UserName?: ")
        if alreadyExists(username):
            print("Username already exists.")
        else:
            exists = False
    password = input("Password?: ")
    email = input("Email?: ")
    print("What is your...")
    first_name = input("First Name?: ")
    last_name = input("Last Name?: ")
    address = input("Address?: ")
    city = input("City?: ")
    state = input("State?: ")
    postal_code = input("Zip Code?: ")
    phone_number = input("Phone Number?: ")
    card_number = input("Card Number?: ")
    card_expiration = input("Card Expiration?: ")
    security_code = input("Card Security Code?: ")
    shoe_size = input("Shoe Size?: ")
    shirt_size = input("Shirt Size?: ")
    pants_size = input("Pants Size?: ")

    post_comp = {
        '_id': username.strip(),
        'password': password.strip(),
        'first_name': first_name.strip(),
        'last_name': last_name.strip(),
        'address': address.strip(),
        'city': city.strip(),
        'state': state.strip(),
        'postal_code': postal_code.strip(),
        'email': email.strip(),
        'phone_number': phone_number.strip(),
        'card_number': card_number.strip(),
        'card_expiration': card_expiration.strip(),
        'security_code': security_code.strip(),
        'shoe_size': shoe_size.strip(),
        'shirt_size': shirt_size.strip(),
        'pants_size': pants_size.strip()
    }

    user_collection.insert_one(post_comp)



def remove_user_from_database(username):
    user_collection.delete_one({'_id'})

sign_up()





