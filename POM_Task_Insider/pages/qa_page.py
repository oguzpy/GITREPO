from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_functions import BaseFunctions
from pages.positions_page import PositionsPages


class QaPages(BaseFunctions):
    """
    Represents a page for Quality Assurance jobs.

    """

    see_all_jobs_btn = (By.XPATH, '//div[contains(@class, "button-group d-flex flex-row")]//a')
    qa_page_title = (By.XPATH, "//h1[contains(@class, 'big-title')][contains(text(),'Quality Assurance')]")

    def __init__(self, driver):
        """
        Initializes the QaPages object.

        :param driver: WebDriver instance.
        """
        super().__init__(driver)
        self.check()

    def check(self):
        """
        Checks for the presence of required elements on the page.

        """
        self.wait.until(EC.element_to_be_clickable(self.see_all_jobs_btn), "See all jobs button not clickable")
        self.wait.until(EC.visibility_of_element_located(self.qa_page_title), "Title is not appear")

    def go_to_all_jobs(self):
        """
        Clicks on "See All Jobs" button.

        :return: PositionsPages object representing the Positions page.
        """
        self.click(self.see_all_jobs_btn)
        return PositionsPages(self.driver)
