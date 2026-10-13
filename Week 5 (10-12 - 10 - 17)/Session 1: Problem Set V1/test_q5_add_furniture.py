from q5_add_furniture import Villager


def test_add_valid_items():
    villager = Villager("Alice", "Koala", "guvnor")
    villager.add_item("acoustic guitar")
    villager.add_item("cacao tree")
    assert villager.furniture == ["acoustic guitar", "cacao tree"]


def test_invalid_item_is_not_added():
    villager = Villager("Alice", "Koala", "guvnor")
    villager.add_item("nintendo switch")
    assert villager.furniture == []