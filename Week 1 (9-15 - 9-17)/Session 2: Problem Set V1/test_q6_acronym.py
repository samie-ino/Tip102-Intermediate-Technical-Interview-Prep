# Edge case: words with mixed case should still produce the correct uppercase acronym.

from q6_acronym import acronym


def test_acronym_basic():
    assert acronym(["Winnie", "the", "Pooh"]) == "WTP"


def test_acronym_mixed_case():
    assert acronym(["winnie", "the", "pooh"]) == "WTP"


def test_acronym_empty():
    assert acronym([]) == ""
