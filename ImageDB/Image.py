import gridfs
import os
from pymongo import MongoClient
from datetime import time
import datetime
import time

product_client = MongoClient(
    'mongodb+srv://qopinstore:%211Supremebot@qop-bot-xe3ad.mongodb.net/test?retryWrites=true&w=majority')
db_products = product_client["Product-DB"]              # database your connecting to
image_collection = db_products["Product-Collection"]    # the collection in the database that's being connected
fs_collection = db_products["fs.chunks"]
fs_files_collection = db_products["fs.files"]

grid_storage = gridfs.GridFS(db_products)               # connection of grid-fs to product database


def add_pics_to_database():
    directory = '/Users/renatabuczkowska/Desktop/qop bot/qopBot/DB_PHOTOS/'

    for image in os.listdir(directory):  # iterates through image file to insert images

        product_image = open(directory + image, 'rb')
        product_data = product_image.read()

        product_post_stored = grid_storage.put(product_data)

        image_str = image.split('.')
        name = image_str[0]

        post_comp = {
            '_id': name,
            'product': product_post_stored
        }

        image_collection.insert_one(post_comp)

def remove_pics_from_database():
    image_collection.delete_many({})
    fs_collection.delete_many({})
    fs_files_collection.delete_many({})


def excecute_collection_reboot(day_of_reboot):
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    if(current_date == day_of_reboot):
        remove_pics_from_database()
        print("Removing last week's inquiries...\n...\n...")
        time.sleep(3)
        print("Adding new photo inquiries...\n...\n...")
        add_pics_to_database()
        time.sleep(1)
        print("Imported photos to database")




def main():
    dropdate = input("When is the date of the next drop? MM-DD-YYYY:\n")
    times = dropdate.split('-')
    db_collection_reboot_day = int(times[1]) - 1
    day_of_reboot = datetime.date(int(times[2]), int(times[0]), db_collection_reboot_day)
    excecute_collection_reboot(day_of_reboot)

main()
