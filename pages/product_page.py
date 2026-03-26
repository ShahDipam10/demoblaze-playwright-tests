from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductPage(BasePage):
    PRODUCT_NAME = ".name"
    PRODUCT_PRICE = ".price-container"
    ADD_TO_CART_BTN = "//a[text()='Add to cart']"

    def __init__(self, page: Page):
        super().__init__(page)

    def get_product_name(self) -> str:
        self.page.wait_for_selector(self.PRODUCT_NAME)
        return self.page.inner_text(self.PRODUCT_NAME)

    def get_product_price(self) -> str:
        self.page.wait_for_selector(self.PRODUCT_PRICE)
        return self.page.inner_text(self.PRODUCT_PRICE)

    def add_to_cart(self):
        self.page.click(self.ADD_TO_CART_BTN)
        self.page.wait_for_event("dialog")

    def add_to_cart_and_accept(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.click(self.ADD_TO_CART_BTN)
        self.page.wait_for_timeout(1000)
