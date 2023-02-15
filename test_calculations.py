import Calculations


def test_calculations():
    assert Calculations.my_add(3, 5) == 8
    assert Calculations.my_subtract(3, 5) == -2
    assert Calculations.my_multiply(3, 5) == 15
    assert Calculations.my_divide(15, 3) == 5

