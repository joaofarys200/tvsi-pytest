import pytest
from calculator import smart_sum

def test_normal_sum():
    assert smart_sum(5, 3) == 8

def test_negative_numbers():
    with pytest.raises(ValueError):
        smart_sum(-1, 5)

def test_zero_pair():
    assert smart_sum(0, 0) == 0

def test_limit_overflow():
    assert smart_sum(80, 50) == 100
