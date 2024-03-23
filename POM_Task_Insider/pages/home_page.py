from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_functions import BaseFunctions
from pages.careers_page import CareersPage


class HomePage(BaseFunctions):
    """
    Represents the Home page.

    """

    navbar_dropdown = (By.ID, 'navbarNavDropdown')
    footer_logo = (By.CLASS_NAME, 'footer_logo')
    company_button = (By.XPATH, '(//*[@class="nav-link dropdown-toggle"])[5]')
    careers_button = (By.XPATH, '//a[text()="Careers"][@class = "dropdown-sub"]')

    def __init__(self, driver):
        """
        Initializes the HomePage object.

        :param driver: WebDriver instance.
        """
        super().__init__(driver)
        self.check()
        self.base_functions = BaseFunctions(self.driver)

    def  check(self):
        """
        Checks for the presence of required sections on the page.

        """
        self.wait.until(EC.visibility_of_element_located(self.navbar_dropdown))
        self.wait.until(EC.visibility_of_element_located(self.footer_logo))

    def go_to_careers_page(self):
        """
        Navigates to the Careers page.

        :return: CareersPage object representing the Careers page.
        """
        self.click(self.company_button)
        self.click(self.careers_button)
        return CareersPage(self.driver)
