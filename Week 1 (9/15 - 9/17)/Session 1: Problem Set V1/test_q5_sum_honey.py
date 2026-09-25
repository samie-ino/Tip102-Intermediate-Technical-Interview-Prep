# Edge case: empty lists and negative values should still add up correctly.

from q5_sum_honey import sum_honey


def test_sum_honey_normal():
    assert sum_honey([12, 7, 31, 5]) == 55


def test_sum_honey_empty():
    assert sum_honey([]) == 0


def test_sum_honey_negative_values():
    assert sum_honey([3, -2, 5]) == 6
