import os
from Utilities.ReadConfiguration import ReadProperties
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AppointmentResults:

    def __init__(self, driver):
        file_path = os.path.relpath(".\\Locators\\locators.ini")
        self._driver = driver
        self.monthlyView = ReadProperties.readConfiguration(file_path, "locators", "btn_MonthlyC_xpath")
        self.btnBook_x = ReadProperties.readConfiguration(file_path, "locators", "btn_book_xpath")
        self.btnBook_c = ReadProperties.readConfiguration(file_path, "locators", "btn_bookA_class")

    def click_monthlyView(self):
        self._driver.find_element(By.XPATH, self.monthlyView).click()

    def click_book(self):
        #self._driver.find_element(By.XPATH, self.btnBook_x).click()
        self._driver.find_element(By.CLASS_NAME, self.btnBook_c).click()

    def click_bookAp(self):
        self._driver.find_element(By.XPATH, self.btnBook_c[1]).click()