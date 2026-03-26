import pytest
from pages.login_page import LoginPage

VALID_USER = "testuser_demo"
VALID_PASS = "Test@1234"

class TestLogin:

    def test_successful_login(self, page):
        login = LoginPage(page)
        login.open()
        login.login(VALID_USER, VALID_PASS)
        assert login.is_logged_in()
        assert "Welcome" in login.get_welcome_text()

    def test_login_shows_username_in_welcome(self, page):
        login = LoginPage(page)
        login.open()
        login.login(VALID_USER, VALID_PASS)
        welcome = login.get_welcome_text()
        assert VALID_USER in welcome

    def test_invalid_credentials_show_alert(self, page):
        login = LoginPage(page)
        login.open()
        login.click_login_nav()
        login.enter_username(VALID_USER)
        login.enter_password("wrongpassword")
        alert_message = []
        page.once("dialog", lambda d: (alert_message.append(d.message), d.accept()))
        page.click(login.SUBMIT_BTN)
        page.wait_for_timeout(2000)
        assert len(alert_message) > 0

    def test_logout_after_login(self, page):
        login = LoginPage(page)
        login.open()
        login.login(VALID_USER, VALID_PASS)
        login.logout()
        page.wait_for_timeout(1000)
        assert not page.is_visible(login.WELCOME_MSG)

    def test_empty_credentials_show_alert(self, page):
        login = LoginPage(page)
        login.open()
        login.click_login_nav()
        alert_message = []
        page.once("dialog", lambda d: (alert_message.append(d.message), d.accept()))
        page.click(login.SUBMIT_BTN)
        page.wait_for_timeout(2000)
        assert len(alert_message) > 0
