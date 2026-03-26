from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.demoblaze.com"
    LOGIN_BTN = "#login2"
    USERNAME_INPUT = "#loginusername"
    PASSWORD_INPUT = "#loginpassword"
    SUBMIT_BTN = "//button[text()='Log in']"
    WELCOME_MSG = "#nameofuser"
    LOGOUT_BTN = "#logout2"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.navigate(self.URL)

    def click_login_nav(self):
        self.page.click(self.LOGIN_BTN)
        self.page.wait_for_selector(self.USERNAME_INPUT, state="visible")

    def enter_username(self, username: str):
        self.page.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_submit(self):
        self.page.click(self.SUBMIT_BTN)

    def login(self, username: str, password: str):
        self.click_login_nav()
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
        self.page.wait_for_selector(self.WELCOME_MSG, timeout=8000)

    def get_welcome_text(self) -> str:
        return self.page.inner_text(self.WELCOME_MSG)

    def is_logged_in(self) -> bool:
        try:
            self.page.wait_for_selector(self.WELCOME_MSG, timeout=5000)
            return self.page.is_visible(self.WELCOME_MSG)
        except Exception:
            return False

    def logout(self):
        self.page.click(self.LOGOUT_BTN)
