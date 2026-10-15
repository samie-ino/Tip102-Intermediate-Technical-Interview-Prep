from q6_find_minimum_in_linked_list import Node, find_min


def test_find_min_returns_smallest_value():
    head1 = Node(5, Node(6, Node(7, Node(8))))
    head2 = Node(8, Node(5, Node(6, Node(7))))

    assert find_min(head1) == 5
    assert find_min(head2) == 5


def test_find_min_empty_list():
    assert find_min(None) is None
