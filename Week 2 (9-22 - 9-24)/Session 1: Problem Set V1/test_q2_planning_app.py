# Edge case: a missing key should be handled carefully instead of crashing.

from q2_planning_app import planning_app


def test_planning_app_basic():
    event = {"name": "Concert", "time": "7:00 PM"}
    assert planning_app(event) == {"name": "Concert", "time": "7:00 PM"}


def test_planning_app_missing_value():
    event = {"name": "Concert"}
    assert planning_app(event) == {"name": "Concert"}
