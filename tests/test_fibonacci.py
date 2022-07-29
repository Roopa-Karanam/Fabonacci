from fibonacci import fibonacci
import pytest

def test_fibonacci_init_():
    assert list(fibonacci(0))==[0]
def test_with_string():
    with pytest.raises(ValueError):
        fibonacci("test")
def test_one():
    assert list(fibonacci(1))==[0,1]
def test_two():
    assert list(fibonacci(2))==[0,1,1]
def test_four():
    assert list(fibonacci(4))==[0,1,1,2,3]



    
  