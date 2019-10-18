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

grid_storage = gridfs.GridFS(database)

def login(user_name, password):
    return

def add_user_to_database():
    return

def remove_user_from_database(username):
    return

#        post_comp = {
#            '_id': name,
#            'product': product_post_stored,
#            'iso': iso[0]


 #       database.insert_one(post_comp)
#





