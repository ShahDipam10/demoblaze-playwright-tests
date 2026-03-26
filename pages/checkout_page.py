from playwright.sync_api import Page
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    NAME_INPUT = "#name"
    COUNTRY_INPUT = "#country"
    CITY_INPUT = "#city"
    CARD_INPUT = "#card"
    MONTH_INPUT = "#month"
    YEAR_INPUT = "#year"
    PURCHASE_BTN = "//button[text()='Purchase']"
    CONFIRM_HEADER = ".sweet-alert h2"
    CONFIRM_TEXT = ".sweet-alert p.lead"
    OK_BTN = ".sweet-alert .confirm"

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_order_form(self, name, country, city, card, month, year):
        self.page.fill(self.NAME_INPUT, name)
        self.page.fill(self.COUNTRY_INPUT, country)
        self.page.fill(self.CITY_INPUT, city)
        self.page.fill(self.CARD_INPUT, card)
        self.page.fill(self.MONTH_INPUT, month)
        self.page.fill(self.YEAR_INPUT, year)

    def click_purchase(self):
        self.page.click(self.PURCHASE_BTN)
        self.page.wait_for_selector(self.CONFIRM_HEADER, timeout=8000)

    def get_confirmation_header(self) -> str:
        return self.page.inner_text(self.CONFIRM_HEADER)

    def get_confirmation_details(self) -> str:
        return self.page.inner_text(self.CONFIRM_TEXT)

    def click_ok(self):
        self.page.click(self.OK_BTN)
        self.page.wait_for_load_state("networkidle")
