from q7_foraging_berries import TreeNode, harvest_berries


def test_harvest_berries_above_threshold():
    bush = TreeNode(
        4,
        TreeNode(10, TreeNode(5), TreeNode(8)),
        TreeNode(6, None, TreeNode(20)),
    )
    assert harvest_berries(bush, 6) == 38


def test_harvest_berries_when_no_values_exceed_threshold():
    bush = TreeNode(4, TreeNode(5), TreeNode(6))
    assert harvest_berries(bush, 30) == 0


def test_harvest_berries_in_empty_tree():
    assert harvest_berries(None, 6) == 0
