from q6_print_inventory import Villager


def test_print_empty_inventory(capsys):
    villager = Villager("Alice", "Koala", "guvnor")
    villager.print_inventory()
    assert capsys.readouterr().out.strip() == "Inventory empty"


def test_print_inventory_counts_items(capsys):
    villager = Villager("Alice", "Koala", "guvnor")
    villager.furniture = [
        "acoustic guitar",
        "ironwood kitchenette",
        "kotatsu",
        "kotatsu",
    ]
    villager.print_inventory()
    assert capsys.readouterr().out.strip() == (
        "acoustic guitar: 1, ironwood kitchenette: 1, kotatsu: 2"
    )