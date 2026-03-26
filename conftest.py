import pytest
from playwright.sync_api import sync_playwright


# Credentials
VALID_USER = "testuser_demo"
VALID_PASS = "Test@1234"

# Fixtures

@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser_instance):
    """Fresh browser context + page for every test."""
    context = browser_instance.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="function")
def logged_in_page(page):
    """Page that is already logged into DemoBlaze."""
    from pages.login_page import LoginPage
    login = LoginPage(page)
    login.open()
    login.login(VALID_USER, VALID_PASS)
    yield page
