# Edge case: repeated house names should count each occurrence, not just unique values.

from q10_eeyores_house import eeyores_house


def test_eeyores_house_basic():
    items = ["Eeyore's house", "Piglet's house", "Eeyore's house"]
    assert eeyores_house(items) == 2


def test_eeyores_house_no_matches():
    items = ["Pooh's house", "Piglet's house"]
    assert eeyores_house(items) == 0


def test_eeyores_house_empty():
    assert eeyores_house([]) == 0
