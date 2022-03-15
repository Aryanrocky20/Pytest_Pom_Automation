import os
from Utilities.ReadConfiguration import ReadProperties
from selenium.webdriver.common.by import By


class PatientHistory:

    def __init__(self, driver):
        file_path = os.path.relpath(".\\Locators\\locators.ini")
        self._driver = driver
        self.bookAppointment = ReadProperties.readConfiguration(file_path, "locators", "button_BookAppointment_class")

    def click_Book(self):
        self._driver.find_element(By.CLASS_NAME, self.bookAppointment).click()
