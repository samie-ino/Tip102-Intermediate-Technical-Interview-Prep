# Edge case: an empty name should still format the greeting with a space before the exclamation.

from q2_greeting import greeting


def test_greeting_output():
    assert greeting("Winnie the Pooh") == "Welcome to The Hundred Acre Wood Winnie the Pooh! My name is Christopher Robin."


def test_greeting_empty_name():
    assert greeting("") == "Welcome to The Hundred Acre Wood ! My name is Christopher Robin."
