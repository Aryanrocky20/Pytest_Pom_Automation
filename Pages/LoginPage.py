import os
from Utilities.ReadConfiguration import ReadProperties
from selenium.webdriver.common.by import By

class Login:

    def __init__(self, driver):
        file_path = os.path.relpath(".\\Locators\\locators.ini")
        self._driver = driver
        self.username = ReadProperties.readConfiguration(file_path, "locators", "textbox_username_name")
        self.password = ReadProperties.readConfiguration(file_path, "locators", "textbox_password_name")
        self.login = ReadProperties.readConfiguration(file_path, "locators", "button_login_class")

    def enter_username(self, user):
        self._driver.find_element(By.NAME, self.username).clear()
        self._driver.find_element(By.NAME, self.username).send_keys(user)

    def enter_password(self, password):
        self._driver.find_element(By.NAME, self.password).clear()
        self._driver.find_element(By.NAME, self.password).send_keys(password)

    def click_login(self):
        self._driver.find_element(By.CLASS_NAME, self.login).click()