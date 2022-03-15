import os
from Utilities.ReadConfiguration import ReadProperties
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AppointmentDetails:

    def __init__(self, driver):
        file_path = os.path.relpath(".\\Locators\\locators.ini")
        self._driver = driver
        self.headingAppointmentDetails = ReadProperties.readConfiguration(file_path, "locators", "heading_AppointmentDetails_xpath")

    def get_AD_test(self):
        return self._driver.find_element(By.XPATH, self.headingAppointmentDetails).text