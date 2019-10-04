#mongo "mongodb+srv://product-images-g8rqq.mongodb.net/admin" --username 1dmironiuk
import pymongo
from pymongo import MongoClient

product_cluster = MongoClient("mongo \"mongodb+srv://product-images-g8rqq.mongodb.net/admin\" --username 1dmironiuk")
db_products = product_cluster["Images"]
db_collection = db_products["Image"]

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












