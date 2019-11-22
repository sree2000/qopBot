import gridfs
import os
from pymongo import MongoClient
from datetime import time
import datetime
import time


product_client = MongoClient(
    'mongodb+srv://qopinstore:%211Supremebot@qop-bot-xe3ad.mongodb.net/test?retryWrites=true&w=majority')
db_products = product_client["Product-DB"]  # database your connecting to
image_collection = db_products["Product-Collection"]  # the collection in the database that's being connected
fs_collection = db_products["fs.chunks"]
fs_files_collection = db_products["fs.files"]
grid_storage = gridfs.GridFS(db_products)
grid_dict = {}


def add_pics_to_database():
    directory = '/Users/renatabuczkowska/Desktop/qop bot/qopBot/DB_PHOTOS/'
    for image in os.listdir(directory):  # iterates through image file to insert images
        if image == ".DS_Store":
            continue
        product_image = open(directory + image, 'rb')
        product_data = product_image.read()

        product_post_stored = grid_storage.put(product_data)

        image_str = image.split('.')
        name = image_str[0]
        iso = name.split('-')

        grid_dict[name] = product_post_stored

        post_comp = {
            '_id': name,
            'product': product_post_stored,
            'iso': iso[0],
        }

        image_collection.insert_one(post_comp)


def remove_pics_from_database():
    image_collection.delete_many({})
    fs_collection.delete_many({})
    fs_files_collection.delete_many({})
    grid_dict.clear()


def get_image(name):
    image = grid_dict[name]
    img = grid_storage.get(image).read()
    return img

def print_pic_inqueries():
    print("What Clothing Items You Can Choose From:\n")
    collection_cursor = image_collection.find({})
    for image in collection_cursor:
        item_name_raw = image['_id']
        if len(item_name_raw) is 0: continue
        proper_arr = item_name_raw.split('-')
        print(proper_arr[0] + ' ' + proper_arr[1])


def choose_image(product_choice):
    synth_jpg = product_choice.split(' ')
    jpg = ''
    for word in synth_jpg:
        jpg += (word + '-')
    final_jpg = jpg[0:len(jpg) - 1]
    return get_image(final_jpg)


def excecute_collection_reboot(day_of_reboot):
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    if (current_date == day_of_reboot):
        remove_pics_from_database()
        print("Removing last week's inquiries...\n...\n...")
        time.sleep(3)
        print("Adding new photo inquiries...\n...\n...")
        add_pics_to_database()
        time.sleep(1)
        print("Imported photos to database")


def main():
    drop_date = input("When is the date of the next drop? MM-DD-YYYY:\n")
    times = drop_date.split('-')
    day_of_reboot = datetime.date(int(times[2]), int(times[0]), int(times[1]))
    excecute_collection_reboot(day_of_reboot)

main()