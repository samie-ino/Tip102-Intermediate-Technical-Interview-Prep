from q6_finding_a_new_plant_within_budget import TreeNode, pick_plant


def test_returns_highest_price_strictly_below_budget():
    inventory = TreeNode(
        50, "Fiddle Leaf Fig",
        TreeNode(25, "Monstera", TreeNode(15, "Aloe"), TreeNode(40, "Pothos")),
        TreeNode(70, "Snake Plant", TreeNode(60, "Fern"), TreeNode(80, "ZZ Plant")),
    )

    assert pick_plant(inventory, 50) == "Pothos"
    assert pick_plant(inventory, 25) == "Aloe"


def test_returns_none_when_no_price_is_strictly_below_budget():
    inventory = TreeNode(15, "Aloe")

    assert pick_plant(inventory, 15) is None
    assert pick_plant(inventory, 10) is None
    assert pick_plant(None, 50) is None
