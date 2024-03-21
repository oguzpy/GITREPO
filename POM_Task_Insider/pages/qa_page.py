from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_functions import BaseFunctions
from pages.positions_page import PositionsPages


class QaPages(BaseFunctions):
    see_all_jobs_btn = (By.XPATH, '//div[contains(@class, "button-group d-flex flex-row")]//a')

    def __init__(self, driver):
        super().__init__(driver)
        self.check()

    def check(self):
        self.wait.until(EC.element_to_be_clickable(self.see_all_jobs_btn), "see all jobs button not clickable")

    def go_to_all_jobs(self):
        self.click(self.see_all_jobs_btn)
        return PositionsPages(self.driver)
