import configparser
import os
import unittest
from selenium import webdriver
import logging

current_dir = os.path.dirname(os.path.abspath(__file__))
settings_file = os.path.join(current_dir, '..', 'base', 'settings.ini')
config = configparser.ConfigParser()
config.read(settings_file)
browser = config.get('WebDriverSettings', 'browser')
site_url = config.get('SiteSettings', 'site_main_url')


class BaseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = self.get_driver(browser)
        self.driver.get(site_url)
        self.driver.maximize_window()
        self.logger = self.init_logger()

    def get_driver(self, driver=browser):
        if driver == 'chrome':
            self.driver = webdriver.Chrome()
        elif driver == 'safari':
            self.driver = webdriver.Safari()
        elif driver == 'firefox':
            self.driver = webdriver.Firefox()
        return self.driver

    def driver_down(self):
        if self.driver:
            self.driver.quit()

    @property
    def test_name(self):
        return self._testMethodName

    def init_logger(self):
        logger = logging.getLogger(self.test_name)
        logger.setLevel(logging.INFO)
        return logger