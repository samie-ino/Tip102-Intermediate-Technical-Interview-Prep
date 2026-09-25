# Edge case: lists with fewer than three items should still be handled cleanly.

from q7_good_things_come_in_threes import good_things_come_in_threes


def test_good_things_come_in_threes_basic():
    assert good_things_come_in_threes([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]


def test_good_things_come_in_threes_short_list():
    assert good_things_come_in_threes([1, 2]) == [[1, 2]]


def test_good_things_come_in_threes_empty():
    assert good_things_come_in_threes([]) == []
