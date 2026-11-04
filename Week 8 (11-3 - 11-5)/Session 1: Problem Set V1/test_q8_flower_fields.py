from q8_flower_fields import TreeNode, find_flower


def test_find_flower_in_tree():
    flower_field = TreeNode(
        "Rose",
        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
        TreeNode("Daisy", None, TreeNode("Dahlia")),
    )
    assert find_flower(flower_field, "Lilac") is True
    assert find_flower(flower_field, "Hibiscus") is False


def test_find_flower_in_empty_tree():
    assert find_flower(None, "Rose") is False
