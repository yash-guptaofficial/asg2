from base_page import BasePage
from locators import ProductPageLocators, NavigationLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductPageLocators()
        self.nav_locators = NavigationLocators()

    def get_all_products(self):
        return self.find_elements(self.locators.PRODUCT_ITEM)

    def get_product_name(self, product_element):
        product_link = product_element.find_element(*self.locators.PRODUCT_LINK)
        return product_link.text

    def get_product_price(self, product_element):
        price_element = product_element.find_element(By.CLASS_NAME, "product-box-list-item-price")
        price_text = price_element.text.split('\n')[0]
        return price_text

    def click_product(self, product_index):
        products = self.get_all_products()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", products[product_index])
        products[product_index].click()

    def add_to_cart_from_list(self, product_index):
        products = self.get_all_products()
        product = products[product_index]
        # Open product detail by clicking product link, then click add-to-cart on product page
        try:
            link = product.find_element(*self.locators.PRODUCT_LINK)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
            link.click()
        except Exception:
            # fallback: click the product container
            self.driver.execute_script("arguments[0].click();", product)

        # On product detail page try to find add-to-cart control with several strategies
        page_xpaths = [
            "//input[contains(@id, 'add-to-cart-button') or contains(@value, 'Add to cart')]",
            "//button[contains(., 'Add to cart')]",
            "//a[contains(., 'Add to cart')]",
            "//*[contains(normalize-space(.), 'Add to cart') and (self::button or self::input or self::a)]",
        ]
        add_button = None
        for xp in page_xpaths:
            try:
                add_button = self.driver.find_element(By.XPATH, xp)
                if add_button:
                    break
            except:
                continue

        if add_button is None:
            # navigate back and raise to make failure obvious
            self.navigate_to_books()
            raise Exception('Add to cart control not found on product detail for index ' + str(product_index))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
        try:
            add_button.click()
        except:
            self.driver.execute_script("arguments[0].click();", add_button)

        # Return to books listing to continue adding next product
        self.navigate_to_books()

    def add_product_to_cart(self):
        self.click_element(self.locators.ADD_TO_CART_BUTTON)

    def navigate_to_books(self):
        self.click_element(self.nav_locators.BOOKS_CATEGORY)

    def go_to_cart(self):
        self.click_element(self.nav_locators.CART_LINK)
        # wait for cart page to load
        try:
            self.wait_for_url_contains('/cart')
        except:
            pass

    def get_cart_count_from_header(self):
        cart_qty = self.get_text(self.nav_locators.CART_LINK)
        count = ''.join(filter(str.isdigit, cart_qty))
        return int(count) if count else 0
