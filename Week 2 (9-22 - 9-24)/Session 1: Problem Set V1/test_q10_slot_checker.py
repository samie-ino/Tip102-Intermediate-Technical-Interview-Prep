# Edge case: touching boundaries should still count as a conflict.

from q10_slot_checker import slot_checker


def test_slot_checker_basic():
    assert slot_checker(1, 4, 2, 5) is True


def test_slot_checker_no_overlap():
    assert slot_checker(1, 2, 3, 4) is False
