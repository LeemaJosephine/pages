from locators.web_locator import SauceDemoLocators


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def enter_credentials(self,username,password):
        self.driver.find_element(SauceDemoLocators.username_locator).send_keys(username)
        self.driver.find_element(*SauceDemoLocators.password_locator).send_keys(password)

    def login(self):
        self.driver.find_element(*SauceDemoLocators.submit_locator).click()

    def is_error_displayed(self):
        self.driver.find_element(*SauceDemoLocators.login_error).is_displayed()

