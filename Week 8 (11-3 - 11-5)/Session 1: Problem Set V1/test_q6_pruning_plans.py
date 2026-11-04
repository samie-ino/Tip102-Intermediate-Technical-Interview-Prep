from q6_pruning_plans import TreeNode, survey_tree


def test_survey_tree_returns_postorder_values():
    magnolia = TreeNode(
        "Root",
        TreeNode("Node1", TreeNode("Leaf1")),
        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
    )
    assert survey_tree(magnolia) == [
        "Leaf1",
        "Node1",
        "Leaf2",
        "Leaf3",
        "Node2",
        "Root",
    ]


def test_survey_empty_tree():
    assert survey_tree(None) == []
