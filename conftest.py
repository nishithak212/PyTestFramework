#Defining Fixtures: Used as setup and tare down methods for test cases.
#conftest file to generalize fixture and make it available to all test cases.
#setup(): This is for setup. Used to invoke browser, set up env variables and so on.
#yield: This is for tear down. Used to close browser and so on


#Data dirven and parameterization can be done with written statements in tuple format

import pytest

#if we want to run the fixture only once before which is setup, the class and once after which is yield, the class is executed we can define
@pytest.fixture(scope="class")
#@pytest.fixture()

def setup(): #setup
    print("I will be executed first")
    yield #tare down. This yield statement makes the code below this line to execute after test_fixtureDemo method is executed
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Winnie","Pooh","test123.com"]

@pytest.fixture(params=[("chrome","Winnie","Pooh"),("Firefox","Winnie"),("Edge","Pooh")])
def crossBrowser(request):
    return request.param


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser selection: chrome or firefox"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = ChromeService("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        driver=webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(8)
    elif browser_name == "firefox":
        service_obj=FirefoxService("C:/Users/nishi/Documents/geckodriver-v0.36.0-win64/geckodriver.exe")
        driver=webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(8)
    # else:
    #     raise ValueError(f"Browser '{browser_name}' not supported")
   # driver.implicitly_wait(8)
    yield driver
    driver.close()