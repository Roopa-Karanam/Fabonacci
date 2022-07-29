"""testing the fibonacci series"""
import pytest
from fibonacci import fibonacci

def test_fibonacci_init_():
    '''testing init'''
    assert list(fibonacci(0))==[0]
def test_with_string():
    '''testing string'''
    with pytest.raises(ValueError):
        fibonacci("test")
def test_one():
    '''testing with one'''
    assert list(fibonacci(1))==[0,1]
def test_two():
    '''testing with 2'''
    assert list(fibonacci(2))==[0,1,1]
def test_four():
    '''testing with 4'''
    assert list(fibonacci(4))==[0,1,1,2,3]
def test_ten():
    '''testing with 10'''
    assert list(fibonacci(10))==[0,1,1,2,3,5,8,13,21,34,55]
def test_negative():
    '''testing negative'''
    assert list(fibonacci(-1))==[]
    