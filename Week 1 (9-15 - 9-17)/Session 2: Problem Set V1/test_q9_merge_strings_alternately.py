# Edge case: if one string is longer, the remaining characters should still be appended.

from q9_merge_strings_alternately import merge_strings_alternately


def test_merge_strings_alternately_basic():
    assert merge_strings_alternately("abc", "defg") == "adbecfg"


def test_merge_strings_alternately_longer_first():
    assert merge_strings_alternately("abcdef", "xy") == "axbycdef"


def test_merge_strings_alternately_empty():
    assert merge_strings_alternately("", "abc") == "abc"
