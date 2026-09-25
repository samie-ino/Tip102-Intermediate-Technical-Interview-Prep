# Edge case: duplicate values should only count once.

from q7_count_unique_species import count_unique_species


def test_count_unique_species_basic():
    species = ["Panda", "Panda", "Snow Leopard", "Sea Turtle", "Sea Turtle"]
    assert count_unique_species(species) == 3


def test_count_unique_species_all_unique():
    species = ["Panda", "Snow Leopard", "Otter"]
    assert count_unique_species(species) == 3
