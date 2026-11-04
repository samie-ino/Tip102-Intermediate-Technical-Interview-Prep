from q4_ivy_cutting_ii import TreeNode, right_vine


def test_right_vine_follows_right_children():
    ivy = TreeNode(
        "Root",
        TreeNode("Node1", TreeNode("Leaf1")),
        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
    )
    assert right_vine(ivy) == ["Root", "Node2", "Leaf3"]


def test_right_vine_stops_when_root_has_no_right_child():
    ivy = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))
    assert right_vine(ivy) == ["Root"]
