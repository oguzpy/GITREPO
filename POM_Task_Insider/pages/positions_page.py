import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_functions import BaseFunctions


class PositionsPages(BaseFunctions):
    location_dropdown = (By.ID, 'select2-filter-by-location-container')
    department_dropdown = (By.ID, 'select2-filter-by-department-container')
    TR_IST_locator = (By.XPATH, "(//li[@id = 'select2-filter-by-location-result-yk97-Istanbul, Turkey'])[1]")
    QA_locator = (By.XPATH, "(//li[@id = 'select2-filter-by-department-result-6u80-Quality Assurance'])[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.check()

    def check(self):
        self.wait.until(EC.element_to_be_clickable(self.location_dropdown), "Location Drop Down not clickable")
        self.wait.until(EC.element_to_be_clickable(self.department_dropdown), "Department Drop Down not clickable")


    def select_location(self):
        self.wait_scroll_and_click_element(self.location_dropdown)
        self.wait_scroll_and_click_element(self.TR_IST_locator)

    def select_department(self):
        self.wait_scroll_and_click_element(self.department_dropdown)
        self.wait_scroll_and_click_element(self.QA_locator)

