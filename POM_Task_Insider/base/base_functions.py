import time
from selenium.common import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseFunctions(object):

    def __init__(self, driver, explicit_wait=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_clickable(self, locator):
        try:
            self.wait.until(ec.element_to_be_clickable(locator))
            return True
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
            return False

    def click(self, selector):
        """
        Wait for element and click
        :param selector: locator of element to find and click
        """
        self.wait.until(ec.element_to_be_clickable(selector)).click()

    def input(self, selector, parameters):
        """
        Wait for element and send parameters
        :param selector: locator of element to find
        :param parameters: It is the parameter that will be sent to selector
        """
        self.wait.until(ec.presence_of_element_located(selector)).send_keys(parameters)

    def wait_for_element(self, selector):
        return self.wait.until(ec.presence_of_element_located(selector))

    def wait_scroll_and_click_element(self, locator, wait_time=1):
        element = self.wait_for_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto' , block: 'center', inline: 'center'});", element)
        time.sleep(wait_time)
        element.click()
        return element

    def refresh_page(self, wait_time=1):
        self.driver.refresh()
        time.sleep(wait_time)

