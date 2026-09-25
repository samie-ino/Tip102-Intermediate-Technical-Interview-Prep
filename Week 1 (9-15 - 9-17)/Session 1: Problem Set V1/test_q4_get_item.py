# Edge case: invalid or negative indices should return None instead of crashing.

from q4_get_item import get_item


def test_valid_index():
    items = ["piglet", "pooh", "roo", "rabbit"]
    assert get_item(items, 2) == "roo"


def test_invalid_index():
    items = ["piglet", "pooh", "roo", "rabbit"]
    assert get_item(items, 10) is None


def test_negative_index():
    items = ["piglet", "pooh", "roo", "rabbit"]
    assert get_item(items, -1) is None
