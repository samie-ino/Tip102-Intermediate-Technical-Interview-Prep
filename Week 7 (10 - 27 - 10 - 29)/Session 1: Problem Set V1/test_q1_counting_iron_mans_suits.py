from q1_counting_iron_mans_suits import (
    count_suits_iterative,
    count_suits_recursive,
)


def test_count_suits_example():
    suits = ["Mark I", "Mark II", "Mark III"]
    assert count_suits_iterative(suits) == 3
    assert count_suits_recursive(suits) == 3


def test_count_suits_empty_list():
    assert count_suits_iterative([]) == 0
    assert count_suits_recursive([]) == 0
