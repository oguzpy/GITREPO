from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_functions import BaseFunctions


class ApplicationPage(BaseFunctions):
    """
    Represents an application page.

    """

    page_headline = (By.CLASS_NAME, 'posting-headline')
    apply_button = (By.CLASS_NAME, 'template-btn-submit')
    page_section = (By.CLASS_NAME, 'template-btn-submit')


    def __init__(self, driver):
        """
        Initializes the ApplicationPage object.

        :param driver: WebDriver instance.
        """
        super().__init__(driver)
        self.check()


    def check(self):
        """
        Checks for the presence of required elements on the page.

        """
        self.wait.until(EC.element_to_be_clickable(self.page_section), "No 'Page Section' in the page!")
        self.wait.until(EC.element_to_be_clickable(self.page_headline), "No 'Page Headline' in the page!")
        self.wait.until(EC.visibility_of_all_elements_located(self.apply_button), "No 'Apply Buttons' in the page!")
