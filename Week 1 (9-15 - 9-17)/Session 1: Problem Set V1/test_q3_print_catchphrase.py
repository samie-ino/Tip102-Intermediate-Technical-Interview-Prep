# Edge case: an unknown character should return the custom sorry message instead of crashing.

from q3_print_catchphrase import print_catchphrase


def test_pooh():
    assert print_catchphrase("Pooh") == "Oh bother!"


def test_tigger():
    assert print_catchphrase("Tigger") == "TTFN: Ta-ta for now!"


def test_eeyore():
    assert print_catchphrase("Eeyore") == "Thanks for noticing me."


def test_christopher_robin():
    assert print_catchphrase("Christopher Robin") == "Silly old bear."


def test_unknown_character():
    assert print_catchphrase("Piglet") == "sorry! I don't know Piglet's catchphrase!"
