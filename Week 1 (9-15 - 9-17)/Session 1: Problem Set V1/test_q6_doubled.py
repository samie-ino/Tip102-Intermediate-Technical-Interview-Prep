# Edge case: empty lists and negative numbers should still be doubled correctly.

from q6_doubled import doubled


def test_doubled_normal():
    assert doubled([1, 2, 3]) == [2, 4, 6]


def test_doubled_empty():
    assert doubled([]) == []


def test_doubled_negative_values():
    assert doubled([-1, 0, 5]) == [-2, 0, 10]
