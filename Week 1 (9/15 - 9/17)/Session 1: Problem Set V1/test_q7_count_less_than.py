# Edge case: values equal to the threshold should not count, but smaller values should.

from q7_count_less_than import count_less_than


def test_count_less_than_basic():
    assert count_less_than([1, 2, 3, 4, 5, 6], 4) == 3


def test_count_less_than_empty():
    assert count_less_than([], 4) == 0


def test_count_less_than_equal_values_do_not_count():
    assert count_less_than([2, 4, 6], 4) == 1
