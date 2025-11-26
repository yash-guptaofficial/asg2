from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "Email")
    PASSWORD_FIELD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Log in']")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button-")
    PRODUCT_ITEM = (By.CLASS_NAME, "product-item")
    PRODUCT_LINK = (By.CLASS_NAME, "product-title")
    ADD_TO_CART_FORM = (By.ID, "add-to-cart")


class CartPageLocators:
    CART_COUNT = (By.CSS_SELECTOR, "span.cart-qty")
    CART_ITEMS = (By.CSS_SELECTOR, "tr[data-productid]")
    ITEM_QUANTITY = (By.CSS_SELECTOR, "input[class*='qty']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "a.product-name")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[name='checkout']")
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div.center p")


class CheckoutPageLocators:
    BILLING_FIRST_NAME = (By.ID, "BillingNewAddress_FirstName")
    BILLING_LAST_NAME = (By.ID, "BillingNewAddress_LastName")
    BILLING_EMAIL = (By.ID, "BillingNewAddress_Email")
    BILLING_PHONE = (By.ID, "BillingNewAddress_PhoneNumber")
    BILLING_COMPANY = (By.ID, "BillingNewAddress_Company")
    BILLING_ADDRESS = (By.ID, "BillingNewAddress_Address1")
    BILLING_CITY = (By.ID, "BillingNewAddress_City")
    BILLING_ZIP = (By.ID, "BillingNewAddress_ZipPostalCode")
    BILLING_STATE = (By.ID, "BillingNewAddress_StateProvinceId")
    BILLING_COUNTRY = (By.ID, "BillingNewAddress_CountryId")
    CONTINUE_BILLING = (By.CSS_SELECTOR, "button[onclick*='Billing']")
    CONTINUE_SHIPPING = (By.CSS_SELECTOR, "button[onclick*='Shipping']")
    CONTINUE_SHIPPING_METHOD = (By.CSS_SELECTOR, "button[onclick*='ShippingMethod']")
    CONTINUE_PAYMENT_METHOD = (By.CSS_SELECTOR, "button[onclick*='PaymentMethod']")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "button[onclick*='ConfirmOrder']")
    ORDER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.section-title")
    ORDER_NUMBER = (By.CSS_SELECTOR, "strong")


class NavigationLocators:
    CART_LINK = (By.CSS_SELECTOR, "a[href='/cart']")
    BOOKS_CATEGORY = (By.XPATH, "//a[contains(text(), 'Books')]")
    HOME_LOGO = (By.CSS_SELECTOR, "a.logo")
