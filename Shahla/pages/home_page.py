from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Shahla.bases.base_page import BasePage
from Shahla.pages.cart_page import CartPage
from Shahla.pages.product_page import ProductPage


class HomePage(BasePage):
    add_to_cart_backpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
    cart_button = (By.CLASS_NAME, 'shopping_cart_container')
    product_name = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.add_to_cart_backpack))
        self.wait.until(ec.visibility_of_element_located(self.cart_button))

    def click_add_to_cart_backpack(self):
        self.driver.find_element(*self.add_to_cart_backpack).click()

    def get_product_name(self):
        return self.driver.find_elements(*self.product_name)[0].text

    def click_cart_button(self):
        self.driver.find_element(*self.cart_button).click()
        return CartPage(self.driver)
