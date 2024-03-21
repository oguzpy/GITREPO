import POM_Task_Insider.base.base_test
from POM_Task_Insider.base.base_test import BaseTest
from POM_Task_Insider.pages.home_page import HomePage
import POM_Task_Insider.base
import pytest

import time


class TestPomViolation(BaseTest):
    def test_(self):
        home_page = HomePage(self.driver)
        careers_page = home_page.go_to_Careers_page()
        qa_page = careers_page.go_to_qa_positions_page()
        positions_page = qa_page.go_to_all_jobs()
        time.sleep(10)
        positions_page.select_location()
        positions_page.select_department()

