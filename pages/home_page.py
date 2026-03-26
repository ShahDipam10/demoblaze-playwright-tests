from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://www.demoblaze.com"
    PRODUCT_CARDS = ".card-title a"
    CART_NAV = "#cartur"
    CATEGORY_PHONES = "//a[text()='Phones']"
    CATEGORY_LAPTOPS = "//a[text()='Laptops']"
    CATEGORY_MONITORS = "//a[text()='Monitors']"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.navigate(self.URL)

    def get_all_product_names(self) -> list:
        self.page.wait_for_selector(self.PRODUCT_CARDS)
        return [el.inner_text() for el in self.page.query_selector_all(self.PRODUCT_CARDS)]

    def click_product_by_name(self, name: str):
        self.page.click(f"//a[text()='{name}']")
        self.page.wait_for_load_state("networkidle")

    def click_first_product(self):
        self.page.wait_for_selector(self.PRODUCT_CARDS)
        self.page.query_selector_all(self.PRODUCT_CARDS)[0].click()
        self.page.wait_for_load_state("networkidle")

    def go_to_cart(self):
        self.page.click(self.CART_NAV)
        self.page.wait_for_load_state("networkidle")

    def filter_by_category(self, category: str):
        selectors = {"phones": self.CATEGORY_PHONES, "laptops": self.CATEGORY_LAPTOPS, "monitors": self.CATEGORY_MONITORS}
        self.page.click(selectors[category.lower()])
        self.page.wait_for_timeout(1500)
