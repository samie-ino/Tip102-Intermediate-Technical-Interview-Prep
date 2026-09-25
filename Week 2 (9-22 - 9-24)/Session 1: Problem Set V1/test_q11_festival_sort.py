# Edge case: already sorted input should remain unchanged.

from q11_festival_sort import festival_sort


def test_festival_sort_basic():
    names = ["Luna", "Milo", "Juno"]
    assert festival_sort(names) == ["Juno", "Luna", "Milo"]


def test_festival_sort_already_sorted():
    names = ["Juno", "Luna", "Milo"]
    assert festival_sort(names) == ["Juno", "Luna", "Milo"]
