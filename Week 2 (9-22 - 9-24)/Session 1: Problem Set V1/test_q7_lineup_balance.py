# Edge case: repeated values should still count correctly without double-counting the same pair.

from q7_lineup_balance import lineup_balance


def test_lineup_balance_basic():
    people = ["A", "B", "A", "C"]
    assert lineup_balance(people) == 2


def test_lineup_balance_empty():
    assert lineup_balance([]) == 0
