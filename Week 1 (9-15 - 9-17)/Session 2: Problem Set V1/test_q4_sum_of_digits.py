# Edge case: numbers with repeated digits should still sum all digits correctly.

from q4_sum_of_digits import sum_of_digits


def test_sum_of_digits_basic():
    assert sum_of_digits(1234) == 10


def test_sum_of_digits_repeated_digits():
    assert sum_of_digits(1111) == 4


def test_sum_of_digits_zero():
    assert sum_of_digits(0) == 0
