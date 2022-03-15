import os
from Utilities.ReadConfiguration import ReadProperties
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AlgoPages:

    def __init__(self, driver):
        file_path = os.path.relpath(".\\Locators\\locators.ini")
        self._driver = driver
        self.specialty = ReadProperties.readConfiguration(file_path, "locators", "dropdown_Specialty_xpath")
        self.bookingDate = ReadProperties.readConfiguration(file_path, "locators", "txtbox_bookingDate_xpath")
        self.next_f = ReadProperties.readConfiguration(file_path, "locators", "btn_Next1_xpath")
        self.DOB = ReadProperties.readConfiguration(file_path, "locators", "txtbox_dob_xpath")
        self.next = ReadProperties.readConfiguration(file_path, "locators", "btn_next_xpath")
        self.previous = ReadProperties.readConfiguration(file_path, "locators", "btn_previous_class")
        self.patientType = ReadProperties.readConfiguration(file_path, "locators", "dropdown_patientType_xpath")
        self.preferredProvider = ReadProperties.readConfiguration(file_path, "locators", "dropdown_preferredP_xpath")
        self.preferredLocation=ReadProperties.readConfiguration(file_path, "locators", "dropdown_location_xpath")
        self.next_class=ReadProperties.readConfiguration(file_path, "locators", "btn_next_class")

    def select_Specialty(self,data):
        element = Select(self._driver.find_element(By.XPATH, self.specialty))
        element.select_by_visible_text(data)

    def enter_bookingDate(self, data):
        self._driver.find_element(By.XPATH, self.bookingDate).clear()
        self._driver.find_element(By.XPATH, self.bookingDate).send_keys(data)

    def click_first_Next(self):
        self._driver.find_element(By.XPATH, self.next_f).click()

    def enter_DOB(self, data):
        self._driver.find_element(By.XPATH, self.DOB).clear()
        self._driver.find_element(By.XPATH, self.DOB).send_keys(data)

    def click_next(self):
        self._driver.find_element(By.XPATH, self.next).click()
        #self._driver.find_element(By.XPATH, self.next_class)[1].click()

    def click_previous(self):
        self._driver.find_element(By.XPATH, self.previous).click()

    def select_PatientType(self,data):
        element = Select(self._driver.find_element(By.XPATH, self.patientType))
        element.select_by_visible_text(data)

    def select_preferredProvider(self,data):
        element = Select(self._driver.find_element(By.XPATH, self.preferredProvider))
        element.select_by_visible_text(data)

    def select_preferredLocation(self,data):
        element = Select(self._driver.find_element(By.XPATH, self.preferredLocation))
        element.select_by_visible_text(data)







