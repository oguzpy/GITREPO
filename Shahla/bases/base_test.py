import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    driver = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\oguzc\PycharmProjects\GITREPO\driver\chromedriver.exe')
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()
