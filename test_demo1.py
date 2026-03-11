#Any pytest file should start with test_ or end with _test keyword

#As per pytest framework standards, code should be written in functions only

#Syntax of funtion in python. Everyline of code should be written in function only if using Pytest framework

#Any code should be wrapped in method only
import pytest
def test_firstProgram(): #Test case name is method name. Test method names should always start with test keyword
    print("Hello Hi")

#Commands to run pytest from terminal

#To run large number of test cases:
#1. pytest == Goes to the directory to find all pytest files
#2. pytest -v == v stands for verbose. Gives more information about test case results execution
#3. pytest -v -s == s is used to print all console logs

#Command to run specific pytest file with filename
#pytest test_demo1.py -v -s

#Command to run specific testcases in pytest
#py.test -k CreditCard -v -s          == k stands for regular expression. Here pytest scans all method names with CreditCard and runs only them

#-k stands for method names execution
#-s stands for logs in output
#-v stands for more info metadata
#-m stands for mark. We can mark tests with @pytest.mark.testtypename e.g. @pytest.mark.smoke
#Skip a test case with @pytest.mark.skip. Can be defined right before the method

@pytest.mark.xfail #Used when we want further test cases to run and do not want this test case to be reported in the result
def test_secondProgram():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])


#Recognizing below test cases as smoke
@pytest.mark.smoke
def test_thirdGreetCreditCard(setup):
    print("Good Afternoon")