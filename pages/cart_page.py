from playwright.sync_api import Page
from pages.base_page import BasePage

class CartPage(BasePage):
    URL = "https://www.demoblaze.com/cart.html"
    CART_ITEMS = "//tbody/tr"
    CART_ITEM_NAMES = "//tbody/tr/td[2]"
    TOTAL_PRICE = "#totalp"
    PLACE_ORDER_BTN = ".btn-success"
    DELETE_BTNS = "//a[text()='Delete']"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.navigate(self.URL)
        self.page.wait_for_load_state("networkidle")

    def get_cart_item_names(self) -> list:
        self.page.wait_for_timeout(1500)
        elements = self.page.query_selector_all(self.CART_ITEM_NAMES)
        return [el.inner_text() for el in elements]

    def get_total_price(self) -> str:
        self.page.wait_for_selector(self.TOTAL_PRICE, timeout=5000)
        return self.page.inner_text(self.TOTAL_PRICE)

    def is_cart_empty(self) -> bool:
        self.page.wait_for_timeout(1500)
        items = self.page.query_selector_all(self.CART_ITEMS)
        return len(items) == 0

    def delete_first_item(self):
        self.page.wait_for_selector(self.DELETE_BTNS)
        self.page.query_selector_all(self.DELETE_BTNS)[0].click()
        self.page.wait_for_timeout(1000)

    def click_place_order(self):
        self.page.click(self.PLACE_ORDER_BTN)
        self.page.wait_for_selector("#orderModal", state="visible")
