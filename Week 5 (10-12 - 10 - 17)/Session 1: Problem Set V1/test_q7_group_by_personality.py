from q7_group_by_personality import Villager, of_personality_type


def test_returns_names_matching_personality():
    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
    stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")
    assert of_personality_type([isabelle, bob, stitches], "Lazy") == [
        "Bob",
        "Stitches",
    ]


def test_no_matches_returns_empty_list():
    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    assert of_personality_type([isabelle], "Cranky") == []