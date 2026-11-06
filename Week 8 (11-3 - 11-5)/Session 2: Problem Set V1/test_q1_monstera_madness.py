from q1_monstera_madness import TreeNode, count_odd_splits


def test_counts_nodes_with_odd_values():
    root = TreeNode(2, TreeNode(3, TreeNode(6), TreeNode(7)), TreeNode(5, None, TreeNode(12)))

    assert count_odd_splits(root) == 3


def test_empty_tree_has_no_odd_splits():
    assert count_odd_splits(None) == 0


def test_single_odd_or_even_node():
    assert count_odd_splits(TreeNode(9)) == 1
    assert count_odd_splits(TreeNode(8)) == 0
