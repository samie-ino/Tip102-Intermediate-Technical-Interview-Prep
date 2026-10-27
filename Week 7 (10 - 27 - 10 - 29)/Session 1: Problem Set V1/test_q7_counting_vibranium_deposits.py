from q7_counting_vibranium_deposits import count_deposits


def test_count_deposits_examples():
    assert count_deposits("VVVVV") == 5
    assert count_deposits("VXVYGA") == 2


def test_count_deposits_without_vibranium():
    assert count_deposits("GOLD") == 0
