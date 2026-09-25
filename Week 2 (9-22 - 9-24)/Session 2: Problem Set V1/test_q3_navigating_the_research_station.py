# Edge case: the start and end locations can be the same, and the route should be a single location.

from q3_navigating_the_research_station import navigate_research_station


def test_navigate_research_station_basic():
    station_map = {
        "lab": ["field", "storage"],
        "field": ["lab", "nursery"],
        "storage": ["lab"],
        "nursery": ["field"]
    }
    assert navigate_research_station(station_map, "lab", "nursery") == ["lab", "field", "nursery"]


def test_navigate_research_station_same_start_end():
    station_map = {"lab": ["field"], "field": ["lab"]}
    assert navigate_research_station(station_map, "lab", "lab") == ["lab"]
