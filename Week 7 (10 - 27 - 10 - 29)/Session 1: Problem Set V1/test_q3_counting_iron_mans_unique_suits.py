from q3_counting_iron_mans_unique_suits import (
    count_suits_iterative,
    count_suits_recursive,
)


def test_count_unique_suits_examples():
    suits = ["Mark I", "Mark I", "Mark III"]
    assert count_suits_iterative(suits) == 2
    assert count_suits_recursive(suits) == 2


def test_count_unique_suits_empty_list():
    assert count_suits_iterative([]) == 0
    assert count_suits_recursive([]) == 0
