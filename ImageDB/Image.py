import gridfs
import os
from pymongo import MongoClient

product_client = MongoClient(
    'mongodb+srv://qopinstore:%211Supremebot@qop-bot-xe3ad.mongodb.net/test?retryWrites=true&w=majority')
db_products = product_client["Product-DB"]                  # database your connecting to
image_collection = db_products["Product-Collection"]       # the collection in the database that's being connected

grid_storage = gridfs.GridFS(db_products)     # connection of grid-fs to product database

directory = '/Users/renatabuczkowska/Desktop/qop bot/qopBot/DB_PHOTOS/'

for image in os.listdir(directory):             # iterates through image file to insert images

    product_image = open(directory + image, 'rb')
    product_data = product_image.read()

    product_post_stored = grid_storage.put(product_data)  # puts image into grid-fs

    image_str = image.split('.')
    name = image_str[0]

    post_comp = {
       '_id': name,
       'product': product_post_stored
    }

    image_collection.insert_one(post_comp)      # adds to the collection


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













