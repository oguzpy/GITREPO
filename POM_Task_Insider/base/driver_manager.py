from selenium import webdriver
from base.base_functions import BaseFunctions as BF
_driver = None

def create_driver():
    global _driver
    if _driver is None:
        _driver = get_driver()
    return _driver

def quit_driver():
    global _driver
    if _driver is not None:
        _driver.quit()
        _driver = None


def get_driver():
    """
    Retrieves the WebDriver based on the configuration.

    :return: WebDriver instance.
    """
    driver = BF.get_set('WebDriverSettings', 'browser')
    if driver == 'chrome':
        driver = webdriver.Chrome()
    elif driver == 'firefox':
        driver = webdriver.Firefox()
    return driver