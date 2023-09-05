import pytest
import json
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.Addtocart import Addtocart

# read login credentials from the JSON file
json_file_path = "/home/emanmhmd/Documents/Projects/Swag_Labs_testing/Fixtures/Data.json"
with open(json_file_path, "r") as json_file:
    Data = json.load(json_file)
# store JSON data in variables
username = Data["credentials"]["username"]
password = Data["credentials"]["password"]
url = Data["URL"]


@pytest.fixture(scope="module")
def driver():
    # set up the webdriver
    driver = webdriver.Chrome()
    # wait some time
    driver.implicitly_wait(10)
    yield driver
    # exit the webdriver
    driver.quit()


# valid login
def login(driver):
    # create an object of the LoginPage class
    login_page = LoginPage(driver)
    # navigate to login page
    driver.get(url)
    # type username and password
    login_page.enter_username(username)
    login_page.enter_password(password)
    # hit on login
    login_page.click_login()


# add items to cart then checkout
def test_add_items_checkout(driver):
    # call login function
    login(driver)
    # create an object of the Addtocart class
    addtocart = Addtocart(driver)
    # call required functions
    addtocart.add_items()
    addtocart.open_cart()
    addtocart.checkout()
    # to logout after done checkout
    addtocart.logout()

