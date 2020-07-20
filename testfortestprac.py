import pytest 
from testprac import add

def test_sum():
    '''Testing if numbers will get sum and if numbers are integers.'''
    num1 = 3
    num2 = 2
    sumofnums = add(num1, num2)
    assert type(sumofnums) == int
    assert sumofnums == 5

def test_int():
    '''testing if input are strings the error is raised.'''
    num1 = "num1"
    num2 = "num2"
    with pytest.raises(Exception) as exc_info:
        if type(num1) == str or type(num2) == str:
            raise Exception("type error")
    exception_raised = exc_info.value
    assert True 



