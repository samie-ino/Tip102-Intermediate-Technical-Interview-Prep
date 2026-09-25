# Edge case: empty or single-character inputs should still be handled safely.

from q5_bouncy_flouncy_trouncy_pouncy import bouncy_flouncy_trouncy_pouncy


def test_bouncy_flouncy_trouncy_pouncy_basic():
    assert bouncy_flouncy_trouncy_pouncy("bouncy") == "bouncy flouncy trouncy pouncy"


def test_bouncy_flouncy_trouncy_pouncy_single_char():
    assert bouncy_flouncy_trouncy_pouncy("a") == "a"


def test_bouncy_flouncy_trouncy_pouncy_empty():
    assert bouncy_flouncy_trouncy_pouncy("") == ""
