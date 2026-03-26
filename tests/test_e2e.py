import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

VALID_USER = "testuser_demo"
VALID_PASS = "Test@1234"

ORDER_DETAILS = {"name": "John Doe", "country": "India", "city": "Ahmedabad", "card": "1234567890123456", "month": "March", "year": "2026"}

class TestE2EFlow:

    def test_browse_products_on_home(self, page):
        home = HomePage(page)
        home.open()
        products = home.get_all_product_names()
        assert len(products) > 0

    def test_filter_by_phones_category(self, page):
        home = HomePage(page)
        home.open()
        home.filter_by_category("phones")
        products = home.get_all_product_names()
        assert len(products) > 0

    def test_add_product_to_cart(self, logged_in_page):
        home = HomePage(logged_in_page)
        home.open()
        home.click_first_product()
        ProductPage(logged_in_page).add_to_cart_and_accept()
        home.go_to_cart()
        cart_items = CartPage(logged_in_page).get_cart_item_names()
        assert len(cart_items) > 0

    def test_cart_shows_correct_product(self, logged_in_page):
        home = HomePage(logged_in_page)
        home.open()
        home.click_first_product()
        product = ProductPage(logged_in_page)
        product_name = product.get_product_name()
        product.add_to_cart_and_accept()
        home.go_to_cart()
        cart_items = CartPage(logged_in_page).get_cart_item_names()
        assert any(product_name in item for item in cart_items)

    def test_delete_item_from_cart(self, logged_in_page):
        home = HomePage(logged_in_page)
        home.open()
        home.click_first_product()
        ProductPage(logged_in_page).add_to_cart_and_accept()
        home.go_to_cart()
        cart = CartPage(logged_in_page)
        cart.delete_first_item()
        assert cart.is_cart_empty()

    def test_full_checkout_flow(self, logged_in_page):
        home = HomePage(logged_in_page)
        home.open()
        home.click_first_product()
        ProductPage(logged_in_page).add_to_cart_and_accept()
        home.go_to_cart()
        cart = CartPage(logged_in_page)
        cart.click_place_order()
        checkout = CheckoutPage(logged_in_page)
        checkout.fill_order_form(**ORDER_DETAILS)
        checkout.click_purchase()
        assert "Thank you" in checkout.get_confirmation_header()
        checkout.click_ok()
