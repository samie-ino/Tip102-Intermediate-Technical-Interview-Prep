from q2_calculating_yield import TreeNode, calculate_yield


def test_calculate_yield_with_each_operator():
    assert calculate_yield(TreeNode("+", TreeNode(7), TreeNode(5))) == 12
    assert calculate_yield(TreeNode("-", TreeNode(7), TreeNode(5))) == 2
    assert calculate_yield(TreeNode("*", TreeNode(7), TreeNode(5))) == 35
    assert calculate_yield(TreeNode("/", TreeNode(8), TreeNode(2))) == 4
