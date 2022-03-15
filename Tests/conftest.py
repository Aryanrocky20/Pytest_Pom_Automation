import time

from selenium import webdriver
import os
import pytest
from Utilities.ReadConfiguration import ReadProperties


def pytest_addoption(parser):
    parser.addoption("--env", action="store")

@pytest.fixture(scope="class")
def getEnv(request):
    _env = request.config.getoption("--env")
    return _env

@pytest.fixture(scope="class")
def setup(request, getEnv):
    _driver = None
    file_path = os.path.relpath(".\\Config\\config.ini")
    if getEnv == "uat":
        base_url = ReadProperties.readConfiguration(file_path, "Configuration", "rd2_url_uat")

    else:
        base_url = ReadProperties.readConfiguration(file_path, "Configuration", "rd2_url_uat")

    _driver = webdriver.Chrome(os.path.relpath(".\\Drivers\\chromedriver.exe"))
    _driver.get(base_url)
    _driver.maximize_window()
    time.sleep(5)
    yield _driver
    _driver.close()