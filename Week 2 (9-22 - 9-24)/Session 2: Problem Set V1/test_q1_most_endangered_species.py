# Edge case: when all scores are equal, the first species should still be returned.

from q1_most_endangered_species import most_endangered_species


def test_most_endangered_species_basic():
    species = ["Snow Leopard", "Giant Panda", "Sea Turtle"]
    risk_scores = [9, 7, 8]
    assert most_endangered_species(species, risk_scores) == "Snow Leopard"


def test_most_endangered_species_tie():
    species = ["Panda", "Sea Turtle"]
    risk_scores = [7, 7]
    assert most_endangered_species(species, risk_scores) == "Panda"
