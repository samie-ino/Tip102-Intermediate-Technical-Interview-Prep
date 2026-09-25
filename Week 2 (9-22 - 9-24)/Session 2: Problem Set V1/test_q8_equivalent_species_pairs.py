# Edge case: a list with no matching duplicates should return zero.

from q8_equivalent_species_pairs import equivalent_species_pairs


def test_equivalent_species_pairs_basic():
    species = ["Panda", "Panda", "Snow Leopard", "Snow Leopard", "Panda"]
    assert equivalent_species_pairs(species) == 3


def test_equivalent_species_pairs_empty():
    assert equivalent_species_pairs([]) == 0
