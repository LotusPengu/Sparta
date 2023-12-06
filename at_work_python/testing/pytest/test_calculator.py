from testing.calculator import *
import pytest


class TestCalculator:

    @pytest.mark.parametrize("num1, num2, expected",
                             [(4, 2, 6), (2, 3, 5), (10, 5, 15)])
    def test_add(self, num1, num2, expected):
        assert add(num1, num2) == expected