from q2_greet_player import Villager, bones


def test_bones_attributes():
    assert bones.name == "Bones"
    assert bones.species == "Dog"
    assert bones.catchphrase == "yip yip"


def test_greet_player():
    villager = Villager("Bones", "Dog", "yip yip")
    assert villager.greet_player("Samia") == (
        "Bones: Hey there, Samia! How's it going, yip yip!"
    )