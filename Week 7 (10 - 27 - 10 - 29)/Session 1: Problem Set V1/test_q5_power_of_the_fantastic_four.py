from q5_power_of_the_fantastic_four import power_of_four


def test_power_of_four_examples():
    assert power_of_four(2) == 16
    assert power_of_four(-2) == 0.0625


def test_power_of_four_zero_exponent():
    assert power_of_four(0) == 1
