# Edge case: 1 should return [1], and larger numbers should list every divisor in ascending order.

from q10_split_haycorns import split_haycorns


def test_split_haycorns_six():
    assert split_haycorns(6) == [1, 2, 3, 6]


def test_split_haycorns_one():
    assert split_haycorns(1) == [1]


def test_split_haycorns_twelve():
    assert split_haycorns(12) == [1, 2, 3, 4, 6, 12]
