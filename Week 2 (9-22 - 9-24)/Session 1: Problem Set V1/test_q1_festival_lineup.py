# Edge case: an empty lineup should still be handled without crashing.

from q1_festival_lineup import festival_lineup


def test_festival_lineup_basic():
    assert festival_lineup(["Milo", "Juno", "Luna"]) == ["Milo", "Juno", "Luna"]


def test_festival_lineup_empty():
    assert festival_lineup([]) == []
