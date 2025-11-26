from base_page import BasePage
from locators import CartPageLocators
from selenium.webdriver.common.by import By
import time


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocators()

    def get_cart_items_count(self):
        try:
            items = self.find_elements(self.locators.CART_ITEMS)
            return len(items)
        except Exception:
            # Fallback: read cart quantity from header (e.g. "(2)")
            try:
                qty_text = self.get_text(self.locators.CART_COUNT)
                count = ''.join(filter(str.isdigit, qty_text))
                return int(count) if count else 0
            except Exception:
                return 0

    def get_cart_items(self):
        cart_items = []
        try:
            items = self.find_elements(self.locators.CART_ITEMS)
            for item in items:
                try:
                    name_element = item.find_element(*self.locators.PRODUCT_NAME)
                    name = name_element.text
                    qty_element = item.find_element(*self.locators.ITEM_QUANTITY)
                    quantity = qty_element.get_attribute('value')
                    cart_items.append({
                        'name': name,
                        'quantity': quantity
                    })
                except:
                    continue
            if cart_items:
                return cart_items
        except:
            pass

        # Fallback: try to gather product names and quantities from page without strict cart row selector
        try:
            name_elements = self.driver.find_elements(By.CSS_SELECTOR, "a.product-name")
            qty_elements = self.driver.find_elements(By.CSS_SELECTOR, "input.qty-input, input[class*='qty'], input[name*='quantity'], input[type='text']")
            for i, ne in enumerate(name_elements):
                try:
                    name = ne.text
                    qty = None
                    if i < len(qty_elements):
                        try:
                            qty = qty_elements[i].get_attribute('value')
                        except:
                            qty = None
                    cart_items.append({'name': name, 'quantity': qty})
                except:
                    continue
        except:
            pass

        return cart_items

    def verify_product_in_cart(self, product_name):
        items = self.get_cart_items()
        pn = product_name.lower()
        for item in items:
            iname = (item.get('name') or '').lower()
            if pn in iname or iname in pn:
                return True
        return False

    def get_product_quantity(self, product_name):
        items = self.get_cart_items()
        pn = product_name.lower()
        for item in items:
            iname = (item.get('name') or '').lower()
            if pn in iname or iname in pn:
                return item.get('quantity')
        return None

    def update_quantity(self, product_name, quantity):
        items = self.find_elements(self.locators.CART_ITEMS)
        for item in items:
            try:
                name_element = item.find_element(*self.locators.PRODUCT_NAME)
                if product_name.lower() in name_element.text.lower():
                    qty_element = item.find_element(*self.locators.ITEM_QUANTITY)
                    qty_element.clear()
                    qty_element.send_keys(str(quantity))
                    break
            except:
                continue

    def proceed_to_checkout(self):
        self.click_element(self.locators.CHECKOUT_BUTTON)

    def is_cart_empty(self):
        return self.is_element_visible(self.locators.CART_EMPTY_MESSAGE)

    def get_cart_total(self):
        try:
            total_element = self.find_element((By.XPATH, "//tr//td[contains(text(), 'Total:')]//following-sibling::td"))
            return total_element.text
        except:
            return None

    def clear_cart(self):
        # navigate to cart page and remove all items if any
        from test_data import TestData
        self.driver.get(TestData.CART_URL)
        time.sleep(1)
        try:
            remove_boxes = self.driver.find_elements(By.NAME, 'removefromcart')
            if remove_boxes:
                for box in remove_boxes:
                    try:
                        if not box.is_selected():
                            box.click()
                    except:
                        continue
                try:
                    update_btn = self.driver.find_element(By.NAME, 'updatecart')
                    update_btn.click()
                except:
                    try:
                        update_btn = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Update shopping cart']")
                        update_btn.click()
                    except:
                        pass
                time.sleep(1)
        except:
            pass
