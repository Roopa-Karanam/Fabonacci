from fibonacci import fibonacci
import pytest

def test_fibonacci_init_():
    assert list(fibonacci(0))==[0]
def test_with_string():
    with pytest.raises(ValueError):
        fibonacci("test")

    
  