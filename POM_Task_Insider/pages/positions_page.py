from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_functions import BaseFunctions
from pages.application_page import ApplicationPage
import time


class PositionsPages(BaseFunctions):
    """
    Represents a page displaying positions.

    """

    result_check = (By.ID, 'deneme')
    location_dropdown_loc = (By.ID, 'select2-filter-by-location-container')
    location_dropdown_menu_loc = (By.CLASS_NAME, 'select2-results__options')
    department_dropdown_loc = (By.ID, 'select2-filter-by-department-container')
    department_dropdown_menu_loc = (By.CLASS_NAME, 'select2-results__options')
    view_role_button = (By.XPATH, "//a[contains(@class, 'btn-navy')][text()='View Role']")
    position_department_text = (By.CSS_SELECTOR, ".position-department")
    position_title_text = (By.CSS_SELECTOR, ".position-title")
    position_location_text = (By.CSS_SELECTOR, ".position-location")
    option_locator = "(//li[text()='{}'])[1]"

    def __init__(self, driver):
        """
        Initializes the PositionsPages object.

        :param driver: WebDriver instance.
        """
        super().__init__(driver)
        self.check()

    def check(self):
        """
        Checks for the presence of required elements on the page.

        """

        self.wait.until(EC.element_to_be_clickable(self.location_dropdown_loc), "Location Drop Down not clickable")
        self.wait.until(EC.element_to_be_clickable(self.department_dropdown_loc), "Department Drop Down not clickable")
        control_result_element = self.wait_for_element(self.result_check)
        self.scroll_and_hover_element(control_result_element)
        self.wait.until(EC.visibility_of_element_located(self.result_check), "Timeout results not found")

    def select_location(self):
        """
        Selects the location from the dropdown menu.

        """
        location = self.get_set('Preferences', 'location')
        if self.wait_for_element(self.location_dropdown_loc).get_attribute("title") == location:
            pass
        else:
            option_locator = (By.XPATH, self.option_locator.format(location))
            self.dropdown_selected_option(self.location_dropdown_loc, self.location_dropdown_menu_loc, option_locator)
            time.sleep(1)

    def select_department(self):
        """
        Selects the department from the dropdown menu.

        """
        department = self.get_set('Preferences', 'department')
        if self.wait_for_element(self.department_dropdown_loc).get_attribute("title") == department:
            pass
        else:
            option_locator = (By.XPATH, self.option_locator.format(department))
            self.dropdown_selected_option(self.department_dropdown_loc, self.department_dropdown_menu_loc,
                                          option_locator)
            time.sleep(1)

    def get_position_boxes_values(self):
        """
        Retrieves values of position boxes.

        :return: List of dictionaries containing position information.
        """
        keys = ['location', 'department', 'title', 'button']
        position_locations = (self.driver.find_elements(*self.position_location_text))
        position_departments = (self.driver.find_elements(*self.position_department_text))
        position_titles = (self.driver.find_elements(*self.position_title_text))
        position_buttons = (self.driver.find_elements(*self.view_role_button))
        results = []
        for location, department, title, button in (
                zip(position_locations, position_departments, position_titles, position_buttons)):
            result = {keys[0]: str(location.text), keys[1]: str(department.text),
                      keys[2]: str(title.text), keys[3]: button}
            results.append(result)
        return results

    def verify_boxes_values(self):
        """
        Verifies the values of position boxes.

        """
        location = self.get_set('Preferences', 'location')
        department = self.get_set('Preferences', 'department')
        boxes = self.get_position_boxes_values()
        for box in boxes:
            if box['location'] == location and box['department'] == department:
                self.assertion_box_button_form(box['button'])
                continue
            else:
                print('Location or Department is not correct' + box['location'] + box['department'])

    def assertion_box_button_form(self, button):
        """
        Asserts the form of box button.

        :param button: The button to be asserted.
        """
        self.scroll_and_hover_element(button)
        self.click(button)
        self.switch_tab(1)
        ApplicationPage(self.driver)
        self.close_tab()
