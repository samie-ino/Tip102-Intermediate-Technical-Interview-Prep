# Edge case: if all values are equal, the function should still return one valid maximum entry.

from q6_performances_with_maximum_audience import performances_with_maximum_audience


def test_performances_with_maximum_audience_basic():
    schedule = {"A": 100, "B": 200, "C": 150}
    assert performances_with_maximum_audience(schedule) == {"B": 200}


def test_performances_with_maximum_audience_tied_values():
    schedule = {"A": 200, "B": 200}
    assert performances_with_maximum_audience(schedule) in ({"A": 200}, {"B": 200})
