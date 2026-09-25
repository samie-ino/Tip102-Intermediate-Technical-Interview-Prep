# Edge case: uppercase and lowercase Tigger letters should both be removed, while other letters stay intact.

from q11_tiggerfy import tiggerfy


def test_tiggerfy_removes_letters():
    assert tiggerfy("suspicerous") == "suspcous"


def test_tiggerfy_all_letters_removed():
    assert tiggerfy("Trigger") == ""


def test_tiggerfy_no_match():
    assert tiggerfy("Hunny") == "Hunny"
