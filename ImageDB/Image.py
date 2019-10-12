import gridfs
import os
import pymongo
from pymongo import MongoClient


product_client = MongoClient(
    'mongodb+srv://1dmironiuk:%211Supremebot@product-images-g8rqq.mongodb.net/test?retryWrites=true&w=majority')
db_products = product_client["Images"]        # database your connecting to
image_collection = db_products["Image"]       # the collection in the database that's being connected

grid_storage = gridfs.GridFS(db_products)     # connection of grid-fs to product database

directory = '/Users/renatabuczkowska/Desktop/qop bot/qopBot/DB_PHOTOS/'

for image in os.listdir(directory):             # iterates through image file

    product_image = open(directory + image, 'rb')
    product_data = product_image.read()
    #product_post_stored = grid_storage.put(product_data)  # puts image into grid-fs

    # out = grid_storage.get(product_post_stored).read()

    #post_comp = {
    #   '_id': 'Orange T-Shirt',        # makes a relation of for the post
    #   'product': product_post_stored
    #}

    #image_collection.insert_one(post_comp)      # adds to the collection


# example on creating a post in the collection {"_id": 0, "name": "Tim", "score": 5}
# insert one post db_collection.insert_one({})
# insert many posts db_collection.insert_many([post1, post2, post3])
# results = db_collection.find({"name" : "bill"})
# for result in results:
#        print(result["name"])      ===> Have to loop because you have to go through the database, finds objects by name
#
# results = db_collection.find_one({"_id":0}) =====> make sure it only finds one by key element without having to loop
#
# db_collection.delete_one({"_id": 1})
# db_collection.delete_many({"_id": 1, 0, 6})
#
# db_collection.update_one({"_id":5}, {$set: {"name":tim}}) ===> finds one person with id 5 and changes their name to tim
# ^^^ Check out update operators for updating a database
#












