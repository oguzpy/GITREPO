# import unittest
# from selenium import webdriver
# from base.base_functions import BaseFunctions
#
#
# class BaseTest(unittest.TestCase, BaseFunctions):
#     """
#     Base test class for setting up test environment and driver.
#
#     """
#
#     def __init__(self, *args, **kwargs):
#         """
#         Initializes the test class.
#
#         :param args: Positional arguments.
#         :param kwargs: Keyword arguments.
#         """
#         super().__init__(*args, **kwargs)
#         site_url = self.get_set('SiteSettings', 'site_main_url')
#         self.driver = self.get_driver()
#         self.driver.get(site_url)
#         self.driver.maximize_window()
#
#
#
#     def driver_down(self):
#         """
#         Quits the WebDriver if it exists.
#
#         """
#         if self.driver:
#             self.driver.quit()
#
#     def take_screenshot(self):
#         """
#         Takes a screenshot and saves it based on the test status.
#
#         :param test_status: The status of the test.
#         """
#         filepath = self.get_set('WebDriverSettings', 'screen_shot_path')
#         filename = f"{filepath}test_result_failed.png"
#         self.driver.save_screenshot(filename)

import unittest
from base.driver_manager import create_driver, quit_driver
from base.base_functions import BaseFunctions


class BaseTest(unittest.TestCase, BaseFunctions):
    """
    Base test class for setting up test environment and driver.
    """
    driver = None

    @classmethod
    def setUpClass(cls):
        # WebDriver örneğini oluştur ve cls.driver değişkenine atama
        cls.driver = create_driver()
        site_url = cls.get_set('SiteSettings', 'site_main_url')
        cls.driver.get(site_url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # WebDriver'ı kapat
        quit_driver()

    @staticmethod
    def take_screenshot():
        """
        Takes a screenshot and saves it based on the test status.

        """
        filepath = BaseTest.get_set('WebDriverSettings', 'screen_shot_path')
        filename = f"{filepath}test_result_failed.png"
        create_driver().save_screenshot(filename)

