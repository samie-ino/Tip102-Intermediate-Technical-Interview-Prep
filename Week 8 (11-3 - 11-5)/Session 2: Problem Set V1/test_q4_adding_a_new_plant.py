from q4_adding_a_new_plant import TreeNode, add_plant


def test_adds_name_to_empty_tree():
    root = add_plant(None, "Aloe")

    assert root is not None
    assert root.val == "Aloe"
    assert root.left is None
    assert root.right is None


def test_adds_name_in_bst_position():
    root = TreeNode("Money Tree", TreeNode("Fiddle Leaf Fig"), TreeNode("Snake Plant"))

    updated = add_plant(root, "Aloe")

    assert updated is root
    assert updated.left.left is not None
    assert updated.left.left.val == "Aloe"


def test_duplicate_is_added_to_existing_nodes_right_subtree():
    root = TreeNode("Rose")

    updated = add_plant(root, "Rose")

    assert updated.right is not None
    assert updated.right.val == "Rose"
