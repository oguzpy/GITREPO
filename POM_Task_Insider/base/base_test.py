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
