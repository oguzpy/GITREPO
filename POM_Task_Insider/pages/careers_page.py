from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from POM_Task_Insider.base.base_functions import BaseFunctions
from POM_Task_Insider.pages.qa_page import QaPages


class CareersPage(BaseFunctions):
    location_sections = (By.ID, 'career-our-location')
    teams_sections = (By.CSS_SELECTOR, '.btn-outline-secondary.loadmore')
    life_at_insider_sections = (By.XPATH, '//h2[contains(@class, "elementor-size-default")][text()="Life at Insider"]')
    qa_job_title = (By.XPATH, '//h3[contains(@class, "text-center mb-4 mb-xl-5")][text()="Quality Assurance"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.check()

    def check(self):
        self.wait.until(EC.visibility_of_element_located(self.location_sections), "Location section is not found")
        self.wait.until(EC.visibility_of_element_located(self.teams_sections), "Teams section is not found")
        self.wait.until(EC.visibility_of_element_located(self.life_at_insider_sections),
                        "Life At Insider section is not found")

    def go_to_qa_positions_page(self):
        self.wait_scroll_and_click_element(self.teams_sections)
        self.wait_scroll_and_click_element(self.qa_job_title)
        return QaPages(self.driver)
