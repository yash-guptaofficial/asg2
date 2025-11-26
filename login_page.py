from base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    def enter_email(self, email):
        self.send_keys(self.locators.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.send_keys(self.locators.PASSWORD_FIELD, password)

    def click_login(self):
        self.click_element(self.locators.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_logged_in(self):
        return self.is_element_visible(self.locators.LOGOUT_LINK)
