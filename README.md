# DemoBlaze Test Automation

Playwright + Python test suite for [DemoBlaze](https://www.demoblaze.com), structured with the **Page Object Model (POM)** pattern.

---

## Setup

```bash
pip install -r requirements.txt
playwright install chromium
pytest
pytest --headed
```

---

## Project Structure

```
demoblaze_tests/
pages/base_page.py
pages/login_page.py
pages/home_page.py
pages/product_page.py
pages/cart_page.py
pages/checkout_page.py
tests/test_login.py
tests/test_e2e.py
conftest.py
pytest.ini
requirements.txt
```

## Test Coverage
- Login: valid/invalid credentials, logout, empty fields
- E2E: browse products, filter categories, add to cart, checkout flow

## Notes
- Update VALID_USER/VALID_PASS in conftest.py with your DemoBlaze account.
- Tests run headless by default.
