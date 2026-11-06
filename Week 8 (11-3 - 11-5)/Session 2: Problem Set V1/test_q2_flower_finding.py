from q2_flower_finding import TreeNode, find_flower


def test_finds_names_in_bst():
    inventory = TreeNode(
        "Rose",
        TreeNode("Lilac", TreeNode("Daisy"), TreeNode("Lily")),
        TreeNode("Tulip", None, TreeNode("Violet")),
    )

    assert find_flower(inventory, "Lilac") is True
    assert find_flower(inventory, "Sunflower") is False


def test_empty_inventory():
    assert find_flower(None, "Rose") is False


def test_finds_root():
    assert find_flower(TreeNode("Rose"), "Rose") is True
