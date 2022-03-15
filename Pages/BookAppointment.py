import os
from Utilities.ReadConfiguration import ReadProperties
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BookAppointment:

    def __init__(self, driver):
        file_path = os.path.relpath(".\\Locators\\locators.ini")
        self._driver = driver
        self.reasonForVisit = ReadProperties.readConfiguration(file_path, "locators", "txtarea_reason_xpath")
        self.customValue = ReadProperties.readConfiguration(file_path, "locators", "txtbox_custom_xpath")
        self.referringProvider = ReadProperties.readConfiguration(file_path, "locators", "txtbox_referringProvider_xpath")
        self.scheduleAppointment = ReadProperties.readConfiguration(file_path, "locators", "btn_schedulAppt_xpath")
        self.customField1 = ReadProperties.readConfiguration(file_path, "locators", "dropdown_customField1_xpath")
        self.customField1btn = ReadProperties.readConfiguration(file_path, "locators", "btn_customField1_xpath")

    def enter_reason(self, data):
        self._driver.find_element(By.XPATH, self.reasonForVisit).clear()
        self._driver.find_element(By.XPATH,self.reasonForVisit).send_keys(data)

    def enter_custom(self, data):
        self._driver.find_element(By.XPATH, self.customValue).clear()
        self._driver.find_element(By.XPATH, self.customValue).send_keys(data)

    def enter_referringProvider(self, data):
        self._driver.find_element(By.XPATH, self.referringProvider).clear()
        self._driver.find_element(By.XPATH, self.referringProvider).send_keys(data)

    def click_scheduleAppointment(self):
        self._driver.find_element(By.XPATH, self.scheduleAppointment).click()

    def click_custom1(self):
        self._driver.find_element(By.XPATH,self.customField1).click()
        keydown = ActionChains(self._driver)
        keydown.send_keys(Keys.ENTER, "Yes").perform()



    def click_custom(self):
        self._driver.find_element(By.XPATH, self.customField1btn).click()


