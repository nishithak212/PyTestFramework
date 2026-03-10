#Any pytest file should start with test_ or end with _test keyword

#As per pytest framework standards, code should be written in functions only

#Syntax of funtion in python. Everyline of code should be written in function only if using Pytest framework

def test_firstProgram(): #Test method. Test method names should always start with test keyword
    print("Hello Hi")

#Commands to run pytest from terminal

#To run large number of test cases:
#1. pytest == Goes to the directory to find all pytest files
#2. pytest -v == v stands for verbose. Gives more information about test case results execution
#3. pytest -v --s == s is used to print all console logs

