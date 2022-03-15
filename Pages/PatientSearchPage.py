import os
from Utilities.ReadConfiguration import ReadProperties
from selenium.webdriver.common.by import By


class PatientSearch:

    def __init__(self, driver):
        file_path = os.path.relpath(".\\Locators\\locators.ini")
        self._driver = driver
        self.FName = ReadProperties.readConfiguration(file_path, "locators", "textbox_FName_xpath")
        self.LName = ReadProperties.readConfiguration(file_path, "locators", "textbox_LName_xpath")
        self.Date = ReadProperties.readConfiguration(file_path, "locators", "textbox_Date_xpath")
        self.MemberID = ReadProperties.readConfiguration(file_path, "locators", "textbox_Member_xpath")
        self.PID = ReadProperties.readConfiguration(file_path, "locators", "textbox_PID_xpath")
        self.SearchPatient = ReadProperties.readConfiguration(file_path, "locators", "button_SearchPatient_xpath")
        self.Reset = ReadProperties.readConfiguration(file_path, "locators", "button_Reset_xpath")
        self.Book = ReadProperties.readConfiguration(file_path, "locators", "button_BookPatient_xpath")
        self.Create = ReadProperties.readConfiguration(file_path, "locators", "link_Create_linktext")


    def enter_Fname(self,data):
        self._driver.find_element(By.XPATH, self.FName).clear()
        self._driver.find_element(By.XPATH, self.FName).send_keys(data)

    def enter_Lname(self,data):
        self._driver.find_element(By.XPATH, self.LName).clear()
        self._driver.find_element(By.XPATH, self.LName).send_keys(data)

    def enter_Date(self,data):
        self._driver.find_element(By.XPATH, self.Date).clear()
        self._driver.find_element(By.XPATH, self.Date).send_keys(data)

    def enter_Member(self,data):
        self._driver.find_element(By.XPATH, self.MemberID).clear()
        self._driver.find_element(By.XPATH, self.MemberID).send_keys(data)

    def enter_PID(self,data):
        self._driver.find_element(By.XPATH, self.PID).clear()
        self._driver.find_element(By.XPATH, self.PID).send_keys(data)

    def click_SearchPatient(self):
        self._driver.find_element(By.XPATH, self.SearchPatient).click()

    def click_Reset(self):
        self._driver.find_element(By.XPATH, self.Reset).click()

    def click_Book(self):
        self._driver.find_element(By.XPATH, self.Book).click()

    def click_Create(self):
        self._driver.find_element(By.LINK_TEXT, self.Create).click()
