from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # define locators using By class
        self.usernameInput = (By.ID, "user-name")
        self.passwordInput = (By.ID, "password")
        self.loginButton = (By.ID, "login-button")

    def enter_username(self, username):
        # type the username into the username input field
        self.driver.find_element(*self.usernameInput).send_keys(username)

    def enter_password(self, password):
        # type the password into the password input field
        self.driver.find_element(*self.passwordInput).send_keys(password)

    def click_login(self):
        # click the login button
        self.driver.find_element(*self.loginButton).click()
