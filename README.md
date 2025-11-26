# E-Commerce Automation Test Suite

Automated test suite for e-commerce flow using Selenium WebDriver and pytest with Page Object Model (POM) pattern.

## Project Structure

```
├── base_page.py           # Base page class with common methods
├── locators.py            # All locators for different pages
├── login_page.py          # Login page object
├── product_page.py        # Product page object
├── cart_page.py           # Cart page object
├── checkout_page.py       # Checkout page object
├── test_data.py           # Test data and configuration
├── test_ecommerce.py      # Main test cases
├── conftest.py            # Pytest configuration
├── requirements.txt       # Project dependencies
└── README.md              # This file
```

## Setup Instructions

1. Install Python 3.8 or higher

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download ChromeDriver:
   - Download from: https://chromedriver.chromium.org/
   - Place in your system PATH or specify path in code

## Running Tests

Run all tests:
```bash
pytest test_ecommerce.py -v
```

Run with detailed output:
```bash
pytest test_ecommerce.py -v -s
```

Run specific test:
```bash
pytest test_ecommerce.py::TestEcommerceFlow::test_login_add_products_and_checkout -v
```

## Test Coverage

The test suite covers:
- Login with valid credentials
- Navigate to products category
- Add two products to cart
- Verify cart count and product details
- Complete checkout with billing information
- Assert order success message

## Page Object Model Benefits

- Centralized locators management
- Reusable methods across test classes
- Easy maintenance and updates
- Clear separation of concerns
- Reduced code duplication
