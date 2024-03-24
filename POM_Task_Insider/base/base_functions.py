from selenium.common import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import configparser
import os


class BaseFunctions(object):
    """
    Defined the basic functions that can be used on all page.

    """

    def __init__(self, driver, explicit_wait=20):
        """
        Inits driver according to explicit wait

        :param driver: Selenium webdriver instance
        :param int explicit_wait: Defined timeout for driver
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def is_element_present(self, element):
        """
        Verify is element present according to given element

        :param WebElement element: Element to be checked
        """
        try:
            self.driver.find_element(*element)
            return True
        except NoSuchElementException:
            return False

    def is_element_clickable(self, element):
        """
        Verify is element clickable according to given element

        :param WebElement element: Element to be checked
        """
        try:
            self.wait.until(ec.element_to_be_clickable(element))
            return True
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
            return False

    def click(self, element):
        """
        Wait for element and click

        :param WebElement element: Element to find and click
        """
        self.wait.until(ec.element_to_be_clickable(element)).click()

    def wait_for_element(self, element):
        """
        Waits for the presence of a specified element.

        :param WebElement element: The element to wait for.
        :return: The element whose presence was awaited.
        """
        return self.wait.until(ec.presence_of_element_located(element))

    def wait_scroll_and_click_element(self, locator, wait_time=1):
        """
        Waits for the element identified by the locator to be clickable after scrolling into view.

        :param locator: Locator of the element to wait for.
        :param wait_time: Optional. Time to wait after scrolling (default is 1 second).
        :return: The clicked element.
        """
        element = self.wait_for_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto' , block: 'center', inline: 'center'});", element)
        time.sleep(wait_time)
        element.click()
        return element

    def dropdown_selected_option(self, dropdown_locator, dropdown_menu_locator, locator_option_text):
        """
        Selects the specified option from the dropdown menu.

        :param dropdown_locator: Locator of the dropdown element.
        :param dropdown_menu_locator: Locator of the dropdown menu.
        :param locator_option_text: Option Locator of the dropdown menu.
        """
        self.wait_scroll_and_click_element(dropdown_locator)
        self.wait_for_element(dropdown_menu_locator)
        option = self.wait_for_element(locator_option_text)
        option.click()

    @staticmethod
    def get_set(settings, key):
        """
        Retrieves a value from the settings file based on the specified settings and key.

        :param settings: Section name in the settings file.
        :param key: Key within the specified section.
        :return: The value corresponding to the specified key in the settings file.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        settings_file = os.path.join(current_dir, '..', 'base', 'settings.ini')
        config = configparser.ConfigParser()
        config.read(settings_file)
        return config.get(settings, key)

    def scroll_and_hover_element(self, element, wait_time=1):
        """
        Scrolls to the specified element and hovers over it.

        :param element: The element to scroll to and hover over.
        :param wait_time: Optional. Time to wait after scrolling (default is 2 seconds).
        """
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto' , block: 'center', inline: 'center'});", element)
        time.sleep(wait_time)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def switch_tab(self, index):
        """
        Switches to the tab specified by its index.

        :param index: Index of the tab to switch to.
        """
        self.driver.switch_to.window(self.driver.window_handles[index])

    def close_tab(self):
        """
        Closes the current tab and switches back to the main window.

        """
        self.driver.execute_script("window.close()")
        self.driver.switch_to.window(self.driver.window_handles[0])