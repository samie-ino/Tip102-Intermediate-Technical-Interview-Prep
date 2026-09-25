# Edge case: the smallest item should be removed while preserving the rest in order.

from q3_delete_minimum import delete_minimum


def test_delete_minimum_basic():
    assert delete_minimum([5, 2, 9, 1, 7]) == [2, 9, 1, 7]


def test_delete_minimum_all_same():
    assert delete_minimum([3, 3, 3]) == [3, 3]


def test_delete_minimum_empty():
    assert delete_minimum([]) == []
