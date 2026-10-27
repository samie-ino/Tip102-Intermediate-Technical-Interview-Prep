from q2_collecting_infinity_stones import sum_stones


def test_sum_stones_examples():
    assert sum_stones([5, 10, 15, 20, 25, 30]) == 105
    assert sum_stones([12, 8, 22, 16, 10]) == 68


def test_sum_stones_empty_list():
    assert sum_stones([]) == 0
