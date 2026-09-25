# Edge case: an empty list should count as valid, but one odd value should make the result False.

from q9_can_pair import can_pair


def test_can_pair_all_even():
    assert can_pair([2, 4, 6, 8]) is True


def test_can_pair_mixed():
    assert can_pair([1, 2, 3, 4]) is False


def test_can_pair_empty():
    assert can_pair([]) is True
