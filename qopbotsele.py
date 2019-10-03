"""
Project: qopbot
Names: Daniel Mironiuk, Jacob Brower, Sreeram Jupudy, Aaron Gdanski
Date: Project start: 02/15/18
Purpose: Creates a local bot algorithm that essentially purchase supreme/ shoes at a very fast pace
file: qopbotsele.py
"""

import time
from PIL import Image
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.select import Select

CONSTANT_TIME = .001
BROWSER = webdriver.Chrome("/Users/renatabuczkowska/Desktop/chromedriver")
TopTypeArr = ["jackets", "shirts", "sweaters", "sweatshirts", "shirts"]
BottomTypeArr = ["shorts", "pants"]

def dictionary(file):
    """
    Creates a dictionary of user information which derives from the file thats
    been called by the main() function
    :param file: the file that contains the user information
    :return: a dictionary that contains client information
    """
    dictionaryUser = dict()
    userDataLine = file.readline().strip().split()
    while userDataLine:
        valueString = ""
        firstWord = userDataLine[0]
        for word in userDataLine:
            if word != firstWord:
                if len(userDataLine) == 2:
                    valueString = valueString + word
                else:
                    valueString = valueString + word + " "
        if len(userDataLine) != 2:
            valueString = valueString[0:len(valueString)-1]
        dictionaryUser[firstWord] = valueString
        userDataLine = file.readline().strip().split()
    return dictionaryUser

def open_browser():
    """
    Opens the chrome browser using it's directory in terminal and using
    the get() command to open such browser
    :return: nothing
    """
    main_sup_page = "https://www.supremenewyork.com/shop/all"
    BROWSER.get(main_sup_page)


def clothing_type(desiredCategory, userInfo):
    cat = desiredCategory.lower().strip()
    if cat in TopTypeArr:
        size = userInfo.get("SIZE_TOPS")
        return size
    if cat in BottomTypeArr:
        size = userInfo.get("SIZE_BOTTOMS")
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
    #image1 = Image.open("image1.jpg")
    #image2 = Image.open("image2.jpg")
    assert image1.mode == image2.mode, "Different kinds of images."
    pairs = zip(image1.getdata(), image2.getdata())
    if len(image1.getbands()) == 1:
    # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    ncomponents = image1.size[0] * image1.size[1] * 3
    return 100-((dif / 255.0 * 100) / ncomponents)

def determination(similarity_percentage):
    """
    determines if the similarity is high enough to determine a matching item
    :param: the similarity precentage
    :return: true if it is above the threshold false otherwise
    """
    threshold = 85.5
    return similarity_percentage > threshold

def interating_through_shop()
    int i = 1
    while(BROWSER.find_element_by_xpath(//div[@id='container']/article[i]/div/a/img).exist())
        #need this to be an image saver
        #image1 will be an image from the website
        #image2 will be a local image that will be the target image
        image1 = BROWSER.find_element_by_xpath(//div[@id='container']/article[8]/div/a/img).click()
        if(determination(compare(image1, image2)))
            #size_scroll() will be called with size and the xpath of the target image and size

def refresh_browser():
    """
    Once clock hits the mark desired it calls this function to refresh the page and then moves
    to the coordinate that makes thr browser full screen
    :return: doesn't return anything
    """
    time.sleep(3)
    BROWSER.refresh()

def size_scroll(clothingSize):
    """
    Accesses the scroll bar and chooses the size in relation
    to the user's size request in their profile
    :return: NONE
    """
    BROWSER.find_element_by_xpath("//img[@alt='Zdtbz1vytcq']").click()
    BROWSER.implicitly_wait(5000)
    scroll = Select(BROWSER.find_element_by_css_selector('#s'))
    scroll.select_by_visible_text(clothingSize.strip())                  # chooses the size of clothing for user


def add_to_cart():
    """
    Adds the current item to your cart so it can begin autofilling
    user information
    :return: NONE
    """
    BROWSER.find_element_by_name("commit").click()
    BROWSER.find_element_by_link_text('checkout now').click()


def product_choice(clothingItem):
    # TODO use the image processing algorithm to find the product desired on the screen
    BROWSER.find_element_by_xpath("//img[@alt='Qdpvgkxh2o8']").click()
    BROWSER.implicitly_wait(5000)
    return clothingItem



def auto_fill(userInfo):
    """
    Used to integrate the users information into the system, allowing the checkout
    process.
    :param userInfo: dictionary of key:value pairs that reflect user information
    :return: NONE
    """
    name = BROWSER.find_element_by_id("order_billing_name")
    name.send_keys(userInfo.get('FIRST_NAME') + ' ' + userInfo.get('LAST_NAME'))
    email = BROWSER.find_element_by_id("order_email")
    email.send_keys(userInfo.get('EMAIL'))
    tel = BROWSER.find_element_by_id("order_tel")
    tel.send_keys(userInfo.get('PHONE_NUMBER'))
    address = BROWSER.find_element_by_id("bo")
    address.send_keys(userInfo.get('ADDRESS'))
    zip = BROWSER.find_element_by_id("order_billing_zip")
    zip.send_keys(userInfo.get('POSTAL_CODE'))
    city = BROWSER.find_element_by_id("order_billing_city")
    city.send_keys(userInfo.get('CITY'))
    state = BROWSER.find_element_by_id("order_billing_state")
    state.send_keys(userInfo.get('STATE'))
    cardNum = BROWSER.find_element_by_id('cnb')
    cardNum.send_keys(userInfo.get('CARD_NUMBER'))
    expireMonth = BROWSER.find_element_by_id("credit_card_month")
    expireMonth.send_keys(userInfo.get('EXPIRATION_MONTH'))
    expireYear = BROWSER.find_element_by_id("credit_card_year")
    expireYear.send_keys(userInfo.get('EXPIRATION_YEAR'))
    cvv = BROWSER.find_element_by_id("vval")
    cvv.send_keys(userInfo.get('SECURITY_CODE'))
    BROWSER.find_element_by_css_selector('.hover > .iCheck-helper').click()
    BROWSER.find_element_by_css_selector('.checkout').click()


def main2():
    file = open("userContstruct.txt")
    userInfo = dictionary(file)
    print("qopbot here at your service!")
    print("[Jackets] [Shirts] [Sweaters] [Sweatshirts] "
          "[Pants] [Shorts] [T-Shirts] [Hats] [Bags] [Accessories] [Skate]")
    clothingCategory = input("What clothing type do you want to qop?\n")             #gets type of clothing user wants
    clothingItem = input("What clothing item do you want to qop?\n")
    clothingColor = input("What clothing color or design would you like today?\n")
    clothingSize = clothing_type(clothingCategory, userInfo)                         # gets size of clothing of user
    open_browser()
    product_choice(clothingItem)
    # TODO create program that goes onto supreme community to get all color configs for each product
    size_scroll(clothingSize)
    BROWSER.implicitly_wait(5000)
    add_to_cart()
    BROWSER.implicitly_wait(5000)
    auto_fill(userInfo)



main2()