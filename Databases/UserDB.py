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


def login(username, password):
    entity = user_collection.find_one({'_id': username})
    exists = True
    while exists:
        if entity == None:
            print("Wrong Username Or Password Please Try Again...")
            username = input("Username?: ")
            password = input("Password?: ")
            continue
        elif entity['_id'] != username or entity['password'] != password:
            print("Wrong Username Or Password Please Try Again...")
            username = input("Username?: ")
            password = input("Password?: ")
            continue
        print("Logging Into qopbot...")
        exists = False
    return entity


def sign_up():
    print("Make a Username and Password...")
    exists = True
    username = input("UserName?: ")
    while exists:
        name = user_collection.find_one({'_id': username})
        if name != None:
            print("Username already exists.")
            username = input("UserName?: ")
        else:
            exists = False
    email = input("Email?: ")
    exists = True
    while exists:
        if user_collection.find_one({'email': email}) != None:
            print("Email already exists.")
            email = input("Email?: ")
        else:
            exists = False
    password = input("Password?: ")
    print("What is your...")
    first_name = input("First Name?: ")
    last_name = input("Last Name?: ")
    address = input("Address?: ")
    city = input("City?: ")
    state = input("State? (i.e. NY): ")
    postal_code = input("Zip Code?: ")
    phone_number = input("Phone Number? (i.e. 8451231234): ")
    card_number = input("Card Number?: ")
    card_expiration = input("Card Expiration? (i.e. 12/21): ")
    card_date = card_expiration.split('/')
    card_month = card_date[0]
    card_year = card_date[1]
    security_code = input("Card Security Code?: ")
    shoe_size = input("Shoe Size? (i.e. 11): ")
    print("Top Size Options (In Type Exactly): [Medium] [Large] [XLarge]")
    shirt_size = input("Shirt Size?: ")
    print("Numerical Pants Size Options (In Type Exactly): [30] [32] [34] [36] [38]")
    pants_size_num = input("Numerical Pants Size?: ")
    print("Textual Pants Size Options (In Type Exactly): [Medium] [Large] [XLarge]")
    pants_size_text = input("Textual Pants Size?: ")

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
        'card_month': card_month,
        'card_year': card_year,
        'security_code': security_code.strip(),
        'shoe_size': shoe_size.strip(),
        'shirt_size': shirt_size.strip(),
        'num_pants_size': pants_size_num.strip(),
        'text_pants_size': pants_size_text.strip()
    }

    user_collection.insert_one(post_comp)

def remove_user_from_database(username, password):
    valid_deletion = input("Do You Want To Delete Your User Info? (Y/N): ")
    if valid_deletion == 'Y':
        print("Deleting...")
        user_collection.delete_one({'_id': username, 'password': password})
    else:
        print("Good Glad You Can Stay!")


def get_user(username):
    if user_collection.find_one({'_id': username}) == None:
        print('User Not In Database...')
    else:
        return user_collection.find_one({'_id': username})

def main():
    validation = input("Do You Have An Account With Us? (Y/N): ")
    if validation == 'Y':
        validation_tree = input("Do You Want To 'LOGIN' or 'DELETE' Account?: ")
        if validation_tree == "LOGIN":
            username = input("Username?: ")
            password = input("Password?: ")
            return login(username, password)
        elif validation_tree == "DELETE":
            username = input("Username?: ")
            password = input("Password?: ")
            remove_user_from_database(username, password)
            return None
    else:
        validation_two = input('Would You Like To Make An Account? (Y/N): ')
        if validation_two == 'Y':
            print("Nice You Now Have An Account Now...")
            sign_up()
            return None
        else:
            print("Going Back To Login...")
            return None
