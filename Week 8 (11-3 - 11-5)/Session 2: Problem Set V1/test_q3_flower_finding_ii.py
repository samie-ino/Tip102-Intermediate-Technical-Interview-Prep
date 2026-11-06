from q3_flower_finding_ii import TreeNode, non_bst_find_flower


def test_finds_name_in_unordered_tree():
    inventory = TreeNode(
        "Daisy",
        TreeNode("Lily", TreeNode("Rose"), TreeNode("Violet")),
        TreeNode("Tulip", None, TreeNode("Lilac")),
    )

    assert non_bst_find_flower(inventory, "Lilac") is True
    assert non_bst_find_flower(inventory, "Sunflower") is False


def test_empty_tree():
    assert non_bst_find_flower(None, "Rose") is False


def test_finds_root():
    assert non_bst_find_flower(TreeNode("Rose"), "Rose") is True
