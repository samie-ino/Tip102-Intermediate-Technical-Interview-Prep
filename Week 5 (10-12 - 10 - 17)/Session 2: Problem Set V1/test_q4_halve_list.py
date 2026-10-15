from q4_halve_list import Node, halve_list


def test_halve_list_divides_each_value_by_two():
    node_one = Node(5)
    node_two = Node(6)
    node_three = Node(7)
    node_one.next = node_two
    node_two.next = node_three

    result = halve_list(node_one)

    assert result.value == 2.5
    assert result.next.value == 3
    assert result.next.next.value == 3.5
