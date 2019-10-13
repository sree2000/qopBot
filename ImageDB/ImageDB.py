import sqlite3
import PIL.Image

connection = sqlite3.connect('Image.py')

connect = connection.cursor()

connect.execute("""CREATE TABLE Image (
    image_name text,
    image text
     )""")

connect.execute("INSERT INTO Image Values ('Yeet', 'Yurt')) ")

connect.execute("SELECT * FROM Image WHERE image_name= 'Yeet'")

connection.commit()

connection.close()