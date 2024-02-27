import time

from Shahla.bases.base_test import BaseTest
from Shahla.pages.login_page import LoginPage


class TestPomViolation(BaseTest):

    def test_pom_violation(self):
        login = LoginPage(self.driver)
        login.enter_user_name('standard_user')
        login.enter_password('secret_sauce')
        home_page = login.click_login_button()
        time.sleep(3)
        name = home_page.get_product_name()
        home_page.click_add_to_cart_backpack()
        home_page.click_cart_button()
        cart = home_page.click_cart_button()
        cart_name = cart.get_item_name()
        self.assertEqual(name, cart_name, "Product is not added to cart")
        time.sleep(5)

