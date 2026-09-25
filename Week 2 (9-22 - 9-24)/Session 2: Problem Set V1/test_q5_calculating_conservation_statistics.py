# Edge case: an empty population dictionary should return zero totals cleanly.

from q5_calculating_conservation_statistics import conservation_statistics


def test_conservation_statistics_basic():
    population_data = {"Snow Leopard": 120, "Sea Turtle": 300, "Panda": 180}
    assert conservation_statistics(population_data) == {"total_population": 600, "species_count": 3}


def test_conservation_statistics_empty():
    assert conservation_statistics({}) == {"total_population": 0, "species_count": 0}
