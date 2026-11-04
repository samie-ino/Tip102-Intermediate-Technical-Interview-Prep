from q5_count_the_tree_leaves import TreeNode, count_leaves


def test_count_leaves_in_tree():
    oak = TreeNode(
        "Root",
        TreeNode("Node1", TreeNode("Leaf1")),
        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
    )
    assert count_leaves(oak) == 3


def test_count_leaves_in_single_node_tree():
    assert count_leaves(TreeNode("Only leaf")) == 1


def test_count_leaves_in_empty_tree():
    assert count_leaves(None) == 0
