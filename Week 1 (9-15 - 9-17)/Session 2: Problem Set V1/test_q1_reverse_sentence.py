# Edge case: empty strings and repeated spaces should still be handled cleanly.

from q1_reverse_sentence import reverse_sentence


def test_reverse_sentence_basic():
    assert reverse_sentence("Winnie the Pooh is hungry") == "hungry is Pooh the Winnie"


def test_reverse_sentence_empty():
    assert reverse_sentence("") == ""


def test_reverse_sentence_extra_spaces():
    assert reverse_sentence("  Pooh   is    hungry  ") == "hungry is Pooh"
