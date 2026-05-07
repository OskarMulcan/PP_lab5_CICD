import pytest
from utils import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)])
def test_add(a, b, expected):
    result = add(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(10, 5, 5), (2, 2, 0), (0, 5, -5)])
def test_subtract(a, b, expected):
    result = subtract(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (4, 5, 20), (0, 10, 0)])
def test_multiply(a, b, expected):
    result = multiply(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(10, 2, 5), (20, 4, 5), (7, 1, 7)])
def test_divide(a, b, expected):
    result = divide(a, b)
    assert result == expected