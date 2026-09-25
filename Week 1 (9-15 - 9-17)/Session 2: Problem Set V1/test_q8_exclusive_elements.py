# Edge case: values shared by both lists should not appear in the result.

from q8_exclusive_elements import exclusive_elements


def test_exclusive_elements_basic():
    assert exclusive_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [1, 2, 5, 6]


def test_exclusive_elements_no_overlap():
    assert exclusive_elements([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_exclusive_elements_empty():
    assert exclusive_elements([], []) == []
