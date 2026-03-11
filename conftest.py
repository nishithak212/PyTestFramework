#Defining Fixtures: Used as setup and tare down methods for test cases.
#conftest file to generalize fixture and make it available to all test cases.
#setup(): This is for setup. Used to invoke browser, set up env variables and so on.
#yield: This is for tare down. Used to close browser and so on


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

