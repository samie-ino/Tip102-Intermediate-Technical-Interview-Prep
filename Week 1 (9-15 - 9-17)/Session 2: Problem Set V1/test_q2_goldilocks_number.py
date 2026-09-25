# Edge case: values outside the valid range should be treated as invalid.

from q2_goldilocks_number import goldilocks_number


def test_goldilocks_number_basic():
    assert goldilocks_number([1, 2, 3, 4, 5]) == 3


def test_goldilocks_number_low_high_outside_range():
    assert goldilocks_number([0, 10]) == 0


def test_goldilocks_number_empty():
    assert goldilocks_number([]) == 0
