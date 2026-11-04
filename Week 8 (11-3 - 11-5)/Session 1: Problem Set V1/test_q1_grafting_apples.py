from q1_grafting_apples import root


def test_grafted_apple_tree():
    assert root.val == "Trunk"
    assert root.left is not None
    assert root.left.val == "Mcintosh"
    assert root.right is not None
    assert root.right.val == "Granny Smith"
    assert root.left.left is not None
    assert root.left.left.val == "Fuji"
    assert root.left.right is not None
    assert root.left.right.val == "Opal"
    assert root.right.left is not None
    assert root.right.left.val == "Crab"
    assert root.right.right is not None
    assert root.right.right.val == "Gala"
