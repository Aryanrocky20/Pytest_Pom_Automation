import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
import os, time
import pytest

booking_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%m/%d/%Y")


print(booking_date)






# driver = webdriver.Chrome(os.path.relpath("C:\\Users\\yash.chindalia\\PycharmProjects\\RD2_test\\Drivers\\chromedriver.exe"))
# driver.get("https://bryandynamic-callcenter-uat.mhddemo.com/")
#
# time.sleep(5)
# driver.find_element(By.NAME, "email").send_keys("yash.chindalia@rsystems.com")
# driver.find_element(By.NAME, "password").send_keys("Hero!@34")
# driver.find_element(By.CLASS_NAME, "loginButton").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//*[@id=\"memberId\"]").send_keys("off001")
# driver.find_element(By.CLASS_NAME, "btn-primary").click()
# time.sleep(5)
# driver.find_element(By.CLASS_NAME, "bookButton").click()
# time.sleep(10)
# items = driver.find_element(By.CLASS_NAME,"btn-primary")
# #driver.find_element(By.CLASS_NAME,"btn-primary")[1].click()
# print(items.text)
# time.sleep(10)
