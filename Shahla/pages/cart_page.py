from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from Shahla.bases.base_page import BasePage

class CartPage(BasePage):

    checkout_button = (By.ID, 'checkout')
    remove_item_button = 'remove-{}'
    item_name = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.checkout_button))
        self.wait.until(ec.visibility_of_element_located(self.item_name))

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()

    def click_remove_item_button(self, product_name):
        self.driver.find_element(By.ID, self.remove_item_button.format(product_name)).click()

    def get_item_name(self):
        return self.driver.find_element(*self.item_name).text
