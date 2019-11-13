"""
Project: qopbot
Names: Daniel Mironiuk, Jacob Brower, Sreeram Jupudy, Aaron Gdanski
Date: Project start: 02/15/18
Purpose: Creates a local bot algorithm that essentially purchase supreme/ shoes at a very fast pace
file: qopbotsele.py
"""
import Databases.ImageDB
import Databases.UserDB
import time
from PIL import Image
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.select import Select

CONSTANT_TIME = .001
BROWSER = webdriver.Chrome("/Users/renatabuczkowska/Desktop/chromedriver")  # CHANGE CHROME DRIVER PATH!!!
TopTypeArr = ["new", "jackets", "shirts", "sweaters", "sweatshirts", "t-shirts"]
BottomTypeArr = ["shorts", "pants"]


def open_browser():
    """
    Opens the chrome browser using it's directory in terminal and using
    the get() command to open such browser
    :return: nothing
    """
    main_sup_page = "https://www.supremenewyork.com/shop/all"
    BROWSER.get(main_sup_page)


def clothing_type(desired_category, user):
    cat = desired_category.lower().strip()
    if cat in TopTypeArr:
        size = user['shirt_size']
        return size
    if cat in BottomTypeArr:
        size = user['num_pants_size']
        return size
    return cat


def clock():
    """
    Doesn't continue until until the clock hits a particular time
    :return: calls the refresh
    """
    now = datetime.now()
    while now.second != 11:
        now = datetime.now()
        print("Current Time (Drop happens at 11pm): %s:%s:%s" % (now.hour, now.minute, now.second))
        time.sleep(1)
    refresh_browser()


def compare(image1, image2):
    """
    compares the two images and determined the similarity percentage
    :param: the two images being compared
    :return: double the similarity percentage
    """
    # image1 = Image.open("image1.jpg")
    # image2 = Image.open("image2.jpg")
    assert image1.mode == image2.mode, "Different kinds of images."
    pairs = zip(image1.getdata(), image2.getdata())
    if len(image1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
    ncomponents = image1.size[0] * image1.size[1] * 3
    return 100 - ((dif / 255.0 * 100) / ncomponents)


def determination(similarity_percentage):
    """
    determines if the similarity is high enough to determine a matching item
    :param: the similarity precentage
    :return: true if it is above the threshold false otherwise
    """
    threshold = 85.5
    return similarity_percentage > threshold


def iterating_through_shop(image_db):
    #image_db must be the image path name
    i = 1
    while BROWSER.find_element_by_css_selector("li:nth-child(" + str(i) + ") img") != 0:
        # image2 will be a local image that will be the target image
        image = BROWSER.find_element_by_css_selector("li:nth-child(" + str(i) + ") img")
        # the line above is a place holder not .get is not something that extracts the image
        # need to get image2
        #add a .screenshot(self, filename)
        image.screenshot("image"+str(i)+".png")
        image1 = Image.open("image"+str(i)+".png")
        if determination(compare(image1, Image.open(image_db))):
            return "li:nth-child(" + str(i) + ") img"
        else:
            i = i + 1


def refresh_browser():
    """
    Once clock hits the mark desired it calls this function to refresh the page and then moves
    to the coordinate that makes thr browser full screen
    :return: doesn't return anything
    """
    time.sleep(3)
    BROWSER.refresh()


def get_product_color(color):
    return ''


def size_scroll(clothing_size):
    """
    Accesses the scroll bar and chooses the size in relation
    to the user's size request in their profile
    :return: NONE
    """
    # BROWSER.find_element_by_xpath("//select[@id='s']").click()
    BROWSER.implicitly_wait(5000)
    # scroll = Select(BROWSER.find_element_by_css_selector('#s'))
    # BROWSER.implicitly_wait(5000)
    # scroll.select_by_visible_text(clothing_size.strip())            # chooses the size of clothing for user


def add_to_cart():
    """
    Adds the current item to your cart so it can begin autofilling
    user information
    :return: NONE
    """
    BROWSER.find_element_by_name("commit").click()
    BROWSER.find_element_by_link_text('checkout now').click()


def product_choice(clothing_item):
    # TODO use the image processing algorithm to find the product desired on the screen
    BROWSER.find_element_by_xpath("//img[@alt='Gdyi96whugc']").click()
    BROWSER.find_element_by_css_selector(iterating_through_shop(clothing_item)).click()
    iterating_through_shop(clothing_item)
    BROWSER.implicitly_wait(5000)
    return clothing_item


def auto_fill(userInfo):
    """
    Used to integrate the users information into the system, allowing the checkout
    process.
    :param userInfo: dictionary of key:value pairs that reflect user information
    :return: NONE
    """
    name = BROWSER.find_element_by_id("order_billing_name")
    name.send_keys(userInfo["first_name"] + ' ' + userInfo["last_name"])
    email = BROWSER.find_element_by_id("order_email")
    email.send_keys(userInfo["email"])
    tel = BROWSER.find_element_by_id("order_tel")
    tel.send_keys(userInfo["phone_number"])
    address = BROWSER.find_element_by_id("bo")
    address.send_keys(userInfo["address"])
    zip = BROWSER.find_element_by_id("order_billing_zip")
    zip.send_keys(userInfo["postal_code"])
    city = BROWSER.find_element_by_id("order_billing_city")
    city.send_keys(userInfo["city"])
    state = BROWSER.find_element_by_id("order_billing_state")
    state.send_keys(userInfo["state"])
    card_num = BROWSER.find_element_by_id('cnb')
    card_num.send_keys(userInfo["card_number"])
    expire_month = BROWSER.find_element_by_id("credit_card_month")
    expire_month.send_keys(userInfo['card_month'])
    expire_year = BROWSER.find_element_by_id("credit_card_year")
    expire_year.send_keys(userInfo['card_year'])
    cvv = BROWSER.find_element_by_id("vval")
    cvv.send_keys(userInfo["security_code"])
    BROWSER.find_element_by_css_selector('.hover > .iCheck-helper').click()
    BROWSER.find_element_by_css_selector('.checkout').click()


def main2():
    print("qopbot here at your service!")
    run_login_id = Databases.UserDB.main()
    while run_login_id == None:
        run_login_id = Databases.UserDB.main()
    update = input("Do you want to update the photo database?\nIf so can only update on dropday (Y/N): ")
    if update == 'Y':
        Databases.ImageDB.main()
    print("__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __")
    Databases.ImageDB.print_pic_inqueries()
    print("__ n__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __")
    clothing_item = input("What clothing item do you want to qop?\n")
    product_image_from_database = Databases.ImageDB.choose_image(clothing_item)
    product_color = product_image_from_database['iso']  # color of product => Orange, Red, NONE
    product_image = product_image_from_database['product']  # prints out ObjectId => 5da941b95af7078d03a97b9c
    print(product_image)
    print("[Jackets] [Shirts] [Sweaters] [Sweatshirts] "
          "[Pants] [Shorts] [T-Shirts] [Hats] [Bags] [Accessories] [Skate]")
    clothing_category = input("What clothing type do you want to qop?\n")  # gets type of clothing user wants
    clothing_size = clothing_type(clothing_category, run_login_id)  # gets size of clothing of user
    open_browser()
    product_choice(product_image)
    size_scroll(clothing_size)
    BROWSER.implicitly_wait(5000)
    add_to_cart()
    BROWSER.implicitly_wait(5000)
    auto_fill(run_login_id)


main2()
