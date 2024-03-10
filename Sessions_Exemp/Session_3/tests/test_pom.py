import unittest
import time

from Sessions_Exemp.Session_3.bases.base_test import BaseTest
from Sessions_Exemp.Session_3.pages.login_page import LoginPage

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPomViolation(BaseTest):

    driver = 'safari'
    def test_pom_violation(self):
        login = LoginPage(self.driver)
        login.enter_user_name('standard_user')
        login.enter_password('secret_sauce')
        home_page = login.click_login_button()
        time.sleep(3)
        name = home_page.get_product_name()
        home_page.click_add_to_cart('backpack')
        cart = home_page.click_cart_button()
        cart_name = cart.get_item_name()
        self.assertEqual(name, cart_name, "Product is not added to cart")
        cart.click_remove_item('backpack')
        self.assertTrue(cart.is_product_removed('backpack'))
        time.sleep(3)


