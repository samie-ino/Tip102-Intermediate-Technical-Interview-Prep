# Problem 3: Navigating the Research Station
# A research station has a map of connected rooms or checkpoints.
# Write a function navigate_research_station(station_map, start, end) that returns the
# shortest valid route from the start location to the end location.
#
# def navigate_research_station(station_map, start, end):
#     pass
#
# Example Usage:
#
# station_map = {
#     "lab": ["field", "storage"],
#     "field": ["lab", "nursery"],
#     "storage": ["lab"],
#     "nursery": ["field"]
# }
# print(navigate_research_station(station_map, "lab", "nursery"))
#
# Example Output:
#
# ["lab", "field", "nursery"]


def navigate_research_station(station_map, start, end):
    pass


if __name__ == "__main__":
    station_map = {
        "lab": ["field", "storage"],
        "field": ["lab", "nursery"],
        "storage": ["lab"],
        "nursery": ["field"]
    }
    print(navigate_research_station(station_map, "lab", "nursery"))
