import pytest
import json
from selenium import webdriver
from Pages.LoginPage import LoginPage

# read login credentials from the JSON file
json_file_path = "/Fixtures/Data.json"
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

# login with right credentials
def test_valid_login(driver):
    # create an object of the LoginPage class
    login_page = LoginPage(driver)
    # navigate to login page
    driver.get(url)
    # type username and password then hit on login
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

# login with wrong credentials
def test_invalid_login(driver):
    # create an object of the LoginPage class
    login_page = LoginPage(driver)
    # navigate to login page
    driver.get(url)
    # type username and wrong password then hit on login
    login_page.enter_username(username)
    login_page.enter_password("wrong-password")
    login_page.click_login()
