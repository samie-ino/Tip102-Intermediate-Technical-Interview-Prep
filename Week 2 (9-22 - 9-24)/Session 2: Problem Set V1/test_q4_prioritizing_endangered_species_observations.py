# Edge case: observations with equal scores should keep their original relative order.

from q4_prioritizing_endangered_species_observations import prioritize_observations


def test_prioritize_observations_basic():
    observations = [
        ["Snow Leopard", 9],
        ["Sea Turtle", 7],
        ["Giant Panda", 8]
    ]
    assert prioritize_observations(observations) == [
        ["Snow Leopard", 9],
        ["Giant Panda", 8],
        ["Sea Turtle", 7]
    ]


def test_prioritize_observations_equal_scores():
    observations = [["Panda", 5], ["Otter", 5], ["Wolf", 3]]
    assert prioritize_observations(observations) == [["Panda", 5], ["Otter", 5], ["Wolf", 3]]
