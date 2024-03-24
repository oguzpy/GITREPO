from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_functions import BaseFunctions
from pages.qa_page import QaPages


class CareersPage(BaseFunctions):
    """
    Represents the Careers page.

    """

    location_sections = (By.ID, 'career-our-location')
    teams_sections = (By.CSS_SELECTOR, '.btn-outline-secondary.loadmore')
    life_at_insider_sections = (By.XPATH, '//h2[contains(@class, "elementor-size-default")][text()="Life at Insider"]')
    qa_job_title = (By.XPATH, '//h3[contains(@class, "text-center mb-4 mb-xl-5")][text()="Quality Assurance"]')

    def __init__(self, driver):
        """
        Initializes the CareersPage object.

        :param driver: WebDriver instance.
        """
        super().__init__(driver)
        self.check()

    def check(self):
        """
        Checks for the presence of required sections on the page.

        """
        self.wait.until(EC.visibility_of_element_located(self.location_sections), "Location section is not found")
        self.wait.until(EC.visibility_of_element_located(self.teams_sections), "Teams section is not found")
        self.wait.until(EC.visibility_of_element_located(self.life_at_insider_sections),
                        "Life At Insider section is not found")

    def go_to_qa_page(self):
        """
        Navigates to the Quality Assurance positions page.

        :return: QaPages object representing the QA positions page.

        """
        self.wait_scroll_and_click_element(self.teams_sections)
        self.wait_scroll_and_click_element(self.qa_job_title)
        return QaPages(self.driver)
