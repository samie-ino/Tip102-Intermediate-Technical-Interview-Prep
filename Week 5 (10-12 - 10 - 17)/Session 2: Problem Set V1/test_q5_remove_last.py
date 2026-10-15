from q5_remove_last import Node, delete_tail


def test_delete_tail_removes_the_last_node():
    butterfly = Node("Common Butterfly")
    ladybug = Node("Ladybug")
    beetle = Node("Scarab Beetle")
    butterfly.next = ladybug
    ladybug.next = beetle

    result = delete_tail(butterfly)

    assert result.value == "Common Butterfly"
    assert result.next.value == "Ladybug"
    assert result.next.next is None


def test_delete_tail_from_single_node_list():
    single = Node("Only")

    assert delete_tail(single) is None
