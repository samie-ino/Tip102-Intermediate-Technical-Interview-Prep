# Edge case: values exactly equal to the threshold should still be included.

from q6_wildlife_reintroduction import wildlife_reintroduction


def test_wildlife_reintroduction_basic():
    species = ["Red Wolf", "Bison", "Fox"]
    habitat_scores = [8, 6, 9]
    assert wildlife_reintroduction(species, habitat_scores, 8) == ["Red Wolf", "Fox"]


def test_wildlife_reintroduction_exact_threshold():
    species = ["Bison", "Otter", "Fox"]
    habitat_scores = [7, 7, 5]
    assert wildlife_reintroduction(species, habitat_scores, 7) == ["Bison", "Otter"]
