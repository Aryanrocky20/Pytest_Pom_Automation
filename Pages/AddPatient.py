import os
from Utilities.ReadConfiguration import ReadProperties
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddPatient:

    def __init__(self, driver):
        file_path = os.path.relpath(".\\Locators\\locators.ini")
        self._driver = driver
        self.FName = ReadProperties.readConfiguration(file_path, "locators", "textbox_FName_xpath")
        self.LName = ReadProperties.readConfiguration(file_path, "locators", "textbox_LName_xpath")
        self.Date = ReadProperties.readConfiguration(file_path, "locators", "textbox_Date_xpath")
        self.MemberID = ReadProperties.readConfiguration(file_path, "locators", "textbox_Member_xpath")
        self.Gender = ReadProperties.readConfiguration(file_path, "locators", "dropdown_gender_xpath")
        self.HPhone = ReadProperties.readConfiguration(file_path, "locators", "textbox_HPhone_xpath")
        self.MPhone = ReadProperties.readConfiguration(file_path, "locators", "textbox_MPhone_xpath")
        self.Address1 = ReadProperties.readConfiguration(file_path, "locators", "textbox_Address1_xpath")
        self.City = ReadProperties.readConfiguration(file_path, "locators", "textbox_City_xpath")
        self.State = ReadProperties.readConfiguration(file_path, "locators", "dropdown_State_xpath")
        self.Zip = ReadProperties.readConfiguration(file_path, "locators", "textbox_Zip_xpath")
        self.Email = ReadProperties.readConfiguration(file_path, "locators", "textbox_Email_xpath")
        self.Save = ReadProperties.readConfiguration(file_path, "locators", "button_Save_xpath")


    def enter_Member(self,data):
        self._driver.find_element(By.XPATH, self.MemberID).clear()
        self._driver.find_element(By.XPATH, self.MemberID).send_keys(data)

    def enter_Fname(self,data):
        self._driver.find_element(By.XPATH, self.FName).clear()
        self._driver.find_element(By.XPATH, self.FName).send_keys(data)

    def enter_Lname(self,data):
        self._driver.find_element(By.XPATH, self.LName).clear()
        self._driver.find_element(By.XPATH, self.LName).send_keys(data)

    def enter_Date(self,data):
        self._driver.find_element(By.XPATH, self.Date).clear()
        self._driver.find_element(By.XPATH, self.Date).send_keys(data)

    def select_Gender(self,data):
        element = Select(self._driver.find_element(By.XPATH, self.Gender))
        element.select_by_visible_text(data)

    def enter_HPhone(self,data):
        self._driver.find_element(By.XPATH, self.HPhone).clear()
        self._driver.find_element(By.XPATH, self.HPhone).send_keys(data)

    def enter_MPhone(self,data):
        self._driver.find_element(By.XPATH, self.MPhone).clear()
        self._driver.find_element(By.XPATH, self.MPhone).send_keys(data)

    def enter_Address1(self, data):
        self._driver.find_element(By.XPATH, self.Address1).clear()
        self._driver.find_element(By.XPATH, self.Address1).send_keys(data)

    def enter_City(self, data):
        self._driver.find_element(By.XPATH, self.City).clear()
        self._driver.find_element(By.XPATH, self.City).send_keys(data)

    def select_State(self, data):
        element = Select(self._driver.find_element(By.XPATH, self.State))
        element.select_by_visible_text(data)

    def enter_Zip(self, data):
        self._driver.find_element(By.XPATH, self.Zip).clear()
        self._driver.find_element(By.XPATH, self.Zip).send_keys(data)

    def enter_Email(self, data):
        self._driver.find_element(By.XPATH, self.Email).clear()
        self._driver.find_element(By.XPATH, self.Email).send_keys(data)

    def click_Save(self):
        self._driver.find_element(By.XPATH, self.Save).click()
