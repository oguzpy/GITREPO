from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from Sessions_Exemp.Session_3.bases.base_page import BasePage
from Sessions_Exemp.Session_3.pages.home_page import HomePage

class LoginPage (BasePage):

    user_name = (By.ID, 'user-name')
    password = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page()

    def wait_page(self):
        self.wait.until(EC.visibility_of_element_located(self.user_name))
        self.wait.until(EC.visibility_of_element_located(self.password))
        self.wait.until(EC.visibility_of_element_located(self.login_button))

    def enter_user_name(self, name):
        self.driver.find_element(*self.user_name).send_keys(name)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
        return HomePage(self.driver)