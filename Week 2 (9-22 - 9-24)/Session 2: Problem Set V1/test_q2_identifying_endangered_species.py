# Edge case: the threshold value should include species with exactly that score.

from q2_identifying_endangered_species import identify_endangered_species


def test_identify_endangered_species_basic():
    species = ["Snow Leopard", "Panda", "Coral Reef"]
    scores = [9, 6, 8]
    assert identify_endangered_species(species, scores, 8) == ["Snow Leopard", "Coral Reef"]


def test_identify_endangered_species_exact_match():
    species = ["Panda", "Sea Turtle", "Otter"]
    scores = [7, 7, 5]
    assert identify_endangered_species(species, scores, 7) == ["Panda", "Sea Turtle"]
