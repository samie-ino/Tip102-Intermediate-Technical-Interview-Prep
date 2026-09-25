# Edge case: when two performers have the same duration, the original order is preserved.

from q12_sort_performers import sort_performers


def test_sort_performers_basic():
    performer_names = ["Mary", "John", "Emma"]
    performance_times = [180, 165, 170]
    assert sort_performers(performer_names, performance_times) == ["Mary", "Emma", "John"]


def test_sort_performers_duplicate_duration():
    performer_names = ["Alice", "Bob", "Bob"]
    performance_times = [155, 185, 150]
    assert sort_performers(performer_names, performance_times) == ["Bob", "Alice", "Bob"]
