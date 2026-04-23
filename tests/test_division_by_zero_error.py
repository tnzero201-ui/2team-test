import pytest

def test_division_by_zero_error():
    with pytest.raises(ZeroDivisionError):
        10 / 0
