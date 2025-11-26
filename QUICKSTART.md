## Quick Start Guide

### 1. Setup Environment
```bash
# Navigate to project directory
cd "/Users/yashgupta/Documents/Vs code/asg-2"

# Install dependencies
pip install -r requirements.txt
```

### 2. Verify ChromeDriver
Ensure ChromeDriver is in your PATH. Test with:
```bash
which chromedriver
```

If not in PATH, download from: https://chromedriver.chromium.org/

### 3. Configure Test Data (if needed)
Edit `test_data.py` to modify:
- Email/password
- Billing information
- Product indices to add
- Base URLs

### 4. Run Tests
```bash
# Run with full output
pytest test_ecommerce.py -v -s

# Run with minimal output
pytest test_ecommerce.py -v

# Run with HTML report
pytest test_ecommerce.py --html=report.html
```

### 5. File Overview

| File | Purpose |
|------|---------|
| locators.py | All element locators |
| base_page.py | Shared page methods |
| login_page.py | Login operations |
| product_page.py | Product browsing |
| cart_page.py | Cart management |
| checkout_page.py | Checkout flow |
| test_ecommerce.py | Test cases |
| test_data.py | Test configuration |
| utils.py | Helper utilities |

### 6. Test Flow

```
Login → Navigate to Products → Add 2 Products → 
Go to Cart → Verify Items → Checkout → 
Fill Billing → Complete Order → Verify Success
```

### 7. Troubleshooting

**ChromeDriver version mismatch:**
Download matching version from chromedriver.chromium.org

**Element not found:**
Check locators.py and inspect element in browser

**Wait timeout:**
Increase wait timeout in base_page.py (default: 10 seconds)

**Login fails:**
Verify credentials in test_data.py match current user
