# Edge case: the function should return the exact welcome string with the correct capitalization and punctuation.

from q1_welcome import welcome


def test_welcome_output():
    assert welcome() == "Welcome to The Hundred Acre Wood!"
