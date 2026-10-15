from q1_mutual_friends import Villager


def test_get_mutuals_basic():
    bob = Villager("Bob", "Cat", "pthhhpth")
    marshal = Villager("Marshal", "Squirrel", "sulky")
    ankha = Villager("Ankha", "Cat", "me meow")
    fauna = Villager("Fauna", "Deer", "dearie")
    raymond = Villager("Raymond", "Cat", "crisp")
    stitches = Villager("Stitches", "Cub", "stuffin")

    bob.friends = [stitches, raymond, fauna]
    marshal.friends = [raymond, ankha, fauna]

    assert bob.get_mutuals(marshal) == ["Raymond", "Fauna"]


def test_get_mutuals_no_overlap():
    bob = Villager("Bob", "Cat", "pthhhpth")
    ankha = Villager("Ankha", "Cat", "me meow")
    marshal = Villager("Marshal", "Squirrel", "sulky")

    bob.friends = [ankha]
    marshal.friends = [Villager("Mabel", "Duck", "quack")]

    assert bob.get_mutuals(marshal) == []
