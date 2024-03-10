from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Sessions_Exemp.Session_3.bases.base_page import BasePage
from Sessions_Exemp.Session_3.pages.cart_page import CartPage
from Sessions_Exemp.Session_3.pages.product_page import ProductPage

class HomePage(BasePage):

    add_to_cart_backpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
    add_to_cart = 'add-to-cart-sauce-labs-{}'
    cart_button = (By.CLASS_NAME, 'shopping_cart_container')
    product_name = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.add_to_cart_backpack))
        self.wait.until(EC.visibility_of_element_located(self.cart_button))

    def click_add_to_cart_backpack(self):
        self.driver.find_element(*self.add_to_cart_backpack).click()

    def click_add_to_cart(self, product):
        self.driver.find_element(By.ID, self.add_to_cart.format(product)).click()
        return ProductPage(self.driver)
    def get_product_name(self):
        return self.driver.find_elements(*self.product_name)[0].text

    def click_cart_button(self):
        self.driver.find_element(*self.cart_button).click()
        return CartPage(self.driver)
