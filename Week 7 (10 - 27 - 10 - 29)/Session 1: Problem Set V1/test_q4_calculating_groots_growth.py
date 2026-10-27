from q4_calculating_groots_growth import fibonacci_growth


def test_fibonacci_growth_examples():
    assert fibonacci_growth(5) == 5
    assert fibonacci_growth(8) == 21


def test_fibonacci_growth_base_cases():
    assert fibonacci_growth(0) == 0
    assert fibonacci_growth(1) == 1
