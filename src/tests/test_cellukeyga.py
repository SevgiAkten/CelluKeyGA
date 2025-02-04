import pytest
from cellukeyga import add_two_digits

def test_add_two_digits_valid():
    assert add_two_digits(23, 45) == 68
    assert add_two_digits(0, 99) == 99
    assert add_two_digits(50, 50) == 100

def test_add_two_digits_invalid():
    with pytest.raises(ValueError):
        add_two_digits(-1, 50)
    with pytest.raises(ValueError):
        add_two_digits(100, 50)
    with pytest.raises(ValueError):
        add_two_digits(50, -1)
    with pytest.raises(ValueError):
        add_two_digits(50, 100)