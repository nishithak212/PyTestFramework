import pytest

#Defining Fixtures: Used as setup and tare down methods for test cases.
#conftest file to generalize fixture and make it available to all test cases.
#setup(): This is for setup. Used to invoke browser, set up env variables and so on.
#yield: This is for tare down. Used to close browser and so on

# @pytest.fixture()
# def setup(): #setup
#     print("I will be executed first")
#     yield #tare down. This yield statement makes the code below this line to execute after test_fixtureDemo method is executed
#     print("I will be executed last")

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute steps in fixture demo method")

    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo3 method")


