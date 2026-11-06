from q7_remove_plant import TreeNode, remove_plant


def test_removes_leaf():
    root = TreeNode("Money Tree", TreeNode("Hoya"), TreeNode("Pilea"))

    updated = remove_plant(root, "Hoya")

    assert updated.left is None


def test_removes_node_with_one_child():
    root = TreeNode("Money Tree", TreeNode("Hoya", None, TreeNode("Ivy")))

    updated = remove_plant(root, "Hoya")

    assert updated.left is not None
    assert updated.left.val == "Ivy"


def test_removes_node_with_two_children_using_inorder_predecessor():
    root = TreeNode(
        "Money Tree",
        TreeNode("Hoya", None, TreeNode("Ivy")),
        TreeNode("Pilea", TreeNode("Orchid"), TreeNode("ZZ Plant")),
    )

    updated = remove_plant(root, "Pilea")

    assert updated.right is not None
    assert updated.right.val == "Orchid"
    assert updated.right.left is None
    assert updated.right.right is not None
    assert updated.right.right.val == "ZZ Plant"


def test_removing_absent_name_keeps_tree():
    root = TreeNode("Rose", TreeNode("Lily"), TreeNode("Tulip"))

    updated = remove_plant(root, "Sunflower")

    assert updated is root
    assert updated.left.val == "Lily"
    assert updated.right.val == "Tulip"


def test_removing_only_root_returns_empty_tree():
    assert remove_plant(TreeNode("Rose"), "Rose") is None
