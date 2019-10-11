# mongo "mongodb+srv://product-images-g8rqq.mongodb.net/admin" --username 1dmironiuk
import pymongo
import gridfs
from pymongo import MongoClient


product_client = MongoClient("mongodb://localhost:4566/")       # connection to the database client
db_products = product_client["Images"]                          # database your connecting to
image_collection = db_products["Image"]                            # the collection in the database that's being connected

product_post = db_products.product_post


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
#
#
#
#












