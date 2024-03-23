import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from base.base_test import BaseTest
from pages.home_page import HomePage
from base import aws_database_controller


class TestPomViolation(BaseTest):
    """
    Test case:
    1) Navigate to Homepage to verify its accessibility.
    2) From the navigation bar, go to the Career page and verify sections are accessible.
    3) Visit the Quality Assurance Careers Page, and verify its accessibility.
    4) Visit the Positions page filter the jobs by location and department,
        check for the job listings' presence.
    5) Ensure each job position lists excepted Position and Department and in the related fields. and verify that
        clicking the "View Role" button navigates to the correct page.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_(self):
        home_page = HomePage(self.driver)
        careers_page = home_page.go_to_careers_page()
        qa_page = careers_page.go_to_qa_page()
        positions_page = qa_page.go_to_all_jobs()
        positions_page.select_location()
        positions_page.select_department()
        positions_page.verify_boxes_values()
        self.driver_down()
        print("Test başarılı !")
