#Any pytest file should start with test_ or end with _test keyword

#As per pytest framework standards, code should be written in functions only

#Syntax of funtion in python. Everyline of code should be written in function only if using Pytest framework.

#Any code should be wrapped in method only

#Commands to run pytest from terminal

#To run large number of test cases:
#1. pytest == Goes to the directory to find all pytest files
#2. pytest -v == v stands for verbose. Gives more information about test case results execution
#3. pytest -v -s == s is used to print all console logs

#Command to run specific pytest file with filename
#pytest test_demo2.py -v -s

#Command to run specific testcases in pytest
#py.test -k CreditCard -v -s  == k stands for regular expression. Here pytest scans all method names with CreditCard and runs only them

#-k stands for method names execution
#-s stands for logs in output
#-v stands for more info metadata
#-m stands for mark. We can mark tests with @pytest.mark.testtypename e.g. @pytest.mark.smoke
#Skip a test case with @pytest.mark.skip. Can be defined right before the method

import pytest

#Recognizing below test cases as smoke
@pytest.mark.smoke
@pytest.mark.skip #Skips the below testcase

def test_firstProgram():
    msg = "Hi"
    assert msg == "Hello" , "Test failed because strings do not match"

def test_secondProgram():
    a=4
    b=6
    assert a+2 == 6, "Addition does not match"

def test_thirdCreditCard():
    a=4
    b=6
    assert a+2 == 8, "Addition does not match"
