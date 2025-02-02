import configparser
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


config = configparser.ConfigParser()
config.read('settings.ini')

browser = config.get(section='WebDriverSettings', option='browser').lower()
window_width = int(config.get(section='WebDriverSettings', option='window_width'))
window_height = int(config.get(section='WebDriverSettings', option='window_height'))


class GoogleSearchPage:
    def __init__(self, web_driver):
        self.driver = web_driver
        self.errors = []

    def open_google(self):
        self.driver.get("https://www.google.com")

    def enter_search_text(self):
        search_text = config.get(section='GoogleSearchSettings', option='search_text')
        textarea = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'gLFyf'))
        )
        textarea.send_keys(search_text)
        textarea.send_keys(Keys.RETURN)
        # WebDriverWait(self.driver, timeout=10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, 'fKmH1e'))
        # )

    def assert_search_result(self):
        textarea_element = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located((By.ID, 'APjFqb'))
        )
        text_value = textarea_element.text
        expected_text = config.get(section='GoogleSearchSettings', option='expected_text')

        if text_value != expected_text:
            message = f"Soft Assertion Failed: Actual text: {text_value}, Excepted text: {expected_text}"
            self.errors.append(message)

    def finalize(self):
        if self.errors:
            error_message = "\n".join(self.errors)
            raise AssertionError(f"Soft assertion failed with the following messages: {error_message}")

    def take_screenshot(self, test_status):
        filepath = config.get(section='WebDriverSettings', option='screen_shot_path')
        filename = f"{filepath}test_result_{test_status}.png"
        self.driver.save_screenshot(filename)

    def close_browser(self):
        self.driver.quit()
        print("Test passed. Browser closed successfully. ")



@pytest.fixture(scope="module")
def driver():
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Invalid browser type: {browser}")
    driver.set_window_size(window_width, window_height)
    yield driver
    driver.quit()


def test_google_search(driver):
    google_search_page = GoogleSearchPage(driver)
    google_search_page.open_google()
    google_search_page.enter_search_text()
    try:
        google_search_page.assert_search_result()
        google_search_page.finalize()

    except AssertionError:
        test_status = "failed2"
        google_search_page.take_screenshot(test_status)
        raise
    finally:
        google_search_page.close_browser()