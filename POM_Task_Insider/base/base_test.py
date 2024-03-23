import unittest
from selenium import webdriver
from base.base_functions import BaseFunctions


class BaseTest(unittest.TestCase, BaseFunctions):
    """
    Base test class for setting up test environment and driver.

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the test class.

        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        site_url = self.get_set('SiteSettings', 'site_main_url')
        self.driver = self.get_driver()
        self.driver.get(site_url)
        self.driver.maximize_window()

    def get_driver(self):
        """
        Retrieves the WebDriver based on the configuration.

        :return: WebDriver instance.
        """
        driver = self.get_set('WebDriverSettings', 'browser')
        if driver == 'chrome':
            self.driver = webdriver.Chrome()
        elif driver == 'safari':
            self.driver = webdriver.Safari()
        elif driver == 'firefox':
            self.driver = webdriver.Firefox()
        return self.driver

    def driver_down(self):
        """
        Quits the WebDriver if it exists.

        """
        if self.driver:
            self.driver.quit()

    def take_screenshot2(self):
        """
        Takes a screenshot and saves it based on the test status.

        :param test_status: The status of the test.
        """
        filepath = self.get_set('WebDriverSettings', 'screen_shot_path')
        filename = f"{filepath}test_result_failed.png"
        self.driver.save_screenshot("teststs.png")