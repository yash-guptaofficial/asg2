import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from product_page import ProductPage
from cart_page import CartPage
from checkout_page import CheckoutPage
from test_data import TestData


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    # headless can be disabled by setting HEADLESS=false in environment
    import os
    headless = os.environ.get("HEADLESS", "true").lower()
    if headless not in ("false", "0", "no"):
        # run headless to allow execution in CI / limited environments
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


class TestEcommerceFlow:
    
    def test_login_add_products_and_checkout(self, driver):
        driver.get(TestData.LOGIN_URL)
        
        login_page = LoginPage(driver)
        assert login_page.is_element_visible(login_page.locators.EMAIL_FIELD), "Login page not loaded properly"
        
        login_page.login(TestData.EMAIL, TestData.PASSWORD)
        assert login_page.is_logged_in(), f"Login failed for user {TestData.EMAIL}"
        
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        # ensure cart is empty before starting
        cart_page.clear_cart()
        product_page.navigate_to_books()
        
        products = product_page.get_all_products()
        assert len(products) > 0, "No products found on page"

        product_names = []
        for index in TestData.PRODUCTS_TO_ADD:
            # refresh product list each iteration to avoid stale element references
            products = product_page.get_all_products()
            product_name = product_page.get_product_name(products[index])
            product_names.append(product_name)
            product_page.add_to_cart_from_list(index)
        
        product_page.go_to_cart()
        
        cart_page = CartPage(driver)
        cart_count = cart_page.get_cart_items_count()
        assert cart_count == 2, f"Expected 2 items in cart, but found {cart_count}"
        
        cart_items = cart_page.get_cart_items()
        for product_name in product_names:
            assert cart_page.verify_product_in_cart(product_name), f"Product {product_name} not found in cart"
        
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) == 2, f"Expected 2 items, but found {len(cart_items)}"
        
        cart_page.proceed_to_checkout()
        
        checkout_page = CheckoutPage(driver)
        billing_info = TestData.BILLING_INFO
        # Some accounts may show an address selection instead of billing form
        if checkout_page.is_element_visible(checkout_page.locators.BILLING_FIRST_NAME):
            checkout_page.fill_billing_address(
                billing_info["first_name"],
                billing_info["last_name"],
                billing_info["email"],
                billing_info["phone"],
                billing_info["company"],
                billing_info["address"],
                billing_info["city"],
                billing_info["zip_code"]
            )

        # attempt to advance through checkout steps resiliently
        success = checkout_page.complete_checkout(max_attempts=8)
        if not success:
            # capture screenshot and page source for debugging
            import os, time
            os.makedirs('artifacts', exist_ok=True)
            ts = time.strftime('%Y%m%d-%H%M%S')
            try:
                driver.save_screenshot(f'artifacts/checkout_failure_{ts}.png')
            except:
                pass
            try:
                with open(f'artifacts/checkout_failure_{ts}.html', 'w', encoding='utf-8') as f:
                    f.write(driver.page_source)
            except:
                pass
            assert success, "Order was not completed successfully"
        
        assert checkout_page.is_order_successful(), "Order was not completed successfully"
        
        success_message = checkout_page.get_success_message()
        assert success_message is not None, "Success message not displayed"
        assert "Thank you" in success_message or "successful" in success_message.lower(), f"Unexpected success message: {success_message}"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
