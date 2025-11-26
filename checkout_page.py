from base_page import BasePage
from locators import CheckoutPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CheckoutPageLocators()

    def fill_billing_address(self, first_name, last_name, email, phone, company, address, city, zip_code, country_id=1, state_id=1):
        self.send_keys(self.locators.BILLING_FIRST_NAME, first_name)
        self.send_keys(self.locators.BILLING_LAST_NAME, last_name)
        self.send_keys(self.locators.BILLING_EMAIL, email)
        self.send_keys(self.locators.BILLING_PHONE, phone)
        self.send_keys(self.locators.BILLING_COMPANY, company)
        self.send_keys(self.locators.BILLING_ADDRESS, address)
        self.send_keys(self.locators.BILLING_CITY, city)
        self.send_keys(self.locators.BILLING_ZIP, zip_code)
        self.select_country(country_id)
        self.select_state(state_id)

    def select_country(self, country_id):
        country_select = self.find_element(self.locators.BILLING_COUNTRY)
        self.driver.execute_script("arguments[0].value = arguments[1];", country_select, str(country_id))
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", country_select)

    def select_state(self, state_id):
        try:
            state_select = self.find_element(self.locators.BILLING_STATE)
            self.driver.execute_script("arguments[0].value = arguments[1];", state_select, str(state_id))
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", state_select)
        except:
            pass

    def continue_billing(self):
        self.scroll_to_element(self.locators.CONTINUE_BILLING)
        self.click_element(self.locators.CONTINUE_BILLING)

    def continue_shipping(self):
        self.scroll_to_element(self.locators.CONTINUE_SHIPPING)
        self.click_element(self.locators.CONTINUE_SHIPPING)

    def continue_shipping_method(self):
        self.scroll_to_element(self.locators.CONTINUE_SHIPPING_METHOD)
        self.click_element(self.locators.CONTINUE_SHIPPING_METHOD)

    def continue_payment_method(self):
        self.scroll_to_element(self.locators.CONTINUE_PAYMENT_METHOD)
        self.click_element(self.locators.CONTINUE_PAYMENT_METHOD)

    def confirm_order(self):
        self.scroll_to_element(self.locators.CONFIRM_ORDER_BUTTON)
        self.click_element(self.locators.CONFIRM_ORDER_BUTTON)

    def is_order_successful(self):
        return self.is_element_visible(self.locators.ORDER_SUCCESS_MESSAGE)

    def get_success_message(self):
        try:
            message = self.get_text(self.locators.ORDER_SUCCESS_MESSAGE)
            return message
        except:
            return None

    def get_order_number(self):
        try:
            numbers = self.find_elements(self.locators.ORDER_NUMBER)
            if len(numbers) > 0:
                return numbers[0].text
        except:
            pass
        return None

    def complete_checkout(self, max_attempts=5):
        # Try to advance through all checkout steps by clicking continue buttons
        import time
        for attempt in range(max_attempts):
            try:
                try:
                    self.continue_billing()
                except:
                    pass
                try:
                    self.continue_shipping()
                except:
                    pass
                try:
                    self.continue_shipping_method()
                except:
                    pass
                try:
                    self.continue_payment_method()
                except:
                    pass
                try:
                    # try to confirm if available
                    self.confirm_order()
                except:
                    pass
                # check if order success shown
                if self.is_order_successful():
                    return True
            except:
                pass
            time.sleep(1)
        return self.is_order_successful()
