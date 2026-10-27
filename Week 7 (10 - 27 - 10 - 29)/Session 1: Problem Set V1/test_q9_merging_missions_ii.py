from q9_merging_missions_ii import Node, merge_missions_iterative


def linked_list_values(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


def test_merge_missions_iterative_example():
    mission1 = Node(1, Node(2, Node(4)))
    mission2 = Node(1, Node(3, Node(4)))

    assert linked_list_values(
        merge_missions_iterative(mission1, mission2)
    ) == [1, 1, 2, 3, 4, 4]


def test_merge_missions_iterative_with_empty_list():
    mission = Node(1, Node(2))

    assert merge_missions_iterative(None, mission) is mission
