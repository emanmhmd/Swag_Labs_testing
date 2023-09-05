import pytest
import json
from selenium import webdriver
from Pages.LoginPage import LoginPage

# Read login credentials from the JSON file
json_file_path = "/home/emanmhmd/Documents/Projects/Swag_Labs_testing/Fixtures/Data.json"
with open(json_file_path, "r") as json_file:
    Data = json.load(json_file)
# Store JSON data in variables
username = Data["credentials"]["username"]
password = Data["credentials"]["password"]
url = Data["URL"]


@pytest.fixture(scope="module")
def driver():
    # Set up the webdriver
    driver = webdriver.Chrome()
    # Wait up to 10 seconds for elements to appear
    driver.implicitly_wait(10)
    yield driver
    # Quit the Selenium webdriver
    driver.quit()

# login with right credentials
def test_valid_login(driver):
    # Create an object of the LoginPage class
    login_page = LoginPage(driver)
    # Open the login page
    driver.get(url)
    # Enter username and password then hit on login
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

# login with wrong credentials
def test_invalid_login(driver):
    # Create an object of the LoginPage class
    login_page = LoginPage(driver)
    # Open the login page
    driver.get(url)
    # Enter username and wrong password then hit on login
    login_page.enter_username(username)
    login_page.enter_password("wrong-password")
    login_page.click_login()
