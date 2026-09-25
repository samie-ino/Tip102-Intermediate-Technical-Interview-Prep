# Edge case: multiple matching thistles should return every index in order, and no matches should return an empty list.

from q12_locate_thistles import locate_thistles


def test_locate_thistles_multiple():
    items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
    assert locate_thistles(items) == [0, 3]


def test_locate_thistles_none():
    items = ["book", "bouncy ball", "leaf", "red balloon"]
    assert locate_thistles(items) == []


def test_locate_thistles_single():
    items = ["leaf", "thistle", "stick"]
    assert locate_thistles(items) == [1]
