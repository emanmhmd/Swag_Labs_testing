from selenium.webdriver.common.by import By
import json

# Read personal info from the JSON file
json_file_path = "/Fixtures/Data.json"
with open(json_file_path, "r") as json_file:
    Data = json.load(json_file)
# Store JSON data in variables
firstname = Data["Personal info"]["First name"]
lastname = Data["Personal info"]["Last name"]
code = Data["Personal info"]["code"]


class Addtocart:
    def __init__(self, driver):
        self.driver = driver
        # define locators using By class
        self.additem1 = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.additem2 = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        self.additem3 = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.cart = (By.ID, "shopping_cart_container")
        self.checkout_button = (By.ID, "checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_shopping = (By.ID, "finish")
        self.confirmation = (By.CLASS_NAME, "complete-header")
        self.burger_menu = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")

    # add items to cart
    def add_items(self):
        self.driver.find_element(*self.additem1).click()
        self.driver.find_element(*self.additem2).click()
        self.driver.find_element(*self.additem3).click()

    # navigate to cart page
    def open_cart(self):
        self.driver.find_element(*self.cart).click()

    def checkout(self):
        # click the checkout button
        self.driver.find_element(*self.checkout_button).click()
        # fill in the first name, last name, and postal code
        self.driver.find_element(*self.first_name).send_keys(firstname)
        self.driver.find_element(*self.last_name).send_keys(lastname)
        self.driver.find_element(*self.postal_code).send_keys(code)
        # click on continue button
        self.driver.find_element(*self.continue_button).click()
        # click the finish button
        self.driver.find_element(*self.finish_shopping).click()

    def get_confirmation_message(self):
        # find and return the text of the confirmation message
        confirmation_element = self.driver.find_element(*self.confirmation)
        return confirmation_element.text

    def assert_confirmation_message(self):
        expected_message = "Thank you for your order!"
        actual_message = self.get_confirmation_message()
        # Assertion on the message
        assert expected_message == actual_message, f"Expected message: {expected_message}, but got: {actual_message}"

    def logout(self):
        # click on burger menu to get expended
        self.driver.find_element(*self.burger_menu).click()
        # click on logout
        self.driver.find_element(*self.logout_button).click()
