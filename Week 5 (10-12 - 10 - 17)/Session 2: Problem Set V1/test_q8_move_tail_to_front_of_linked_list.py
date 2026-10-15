from q8_move_tail_to_front_of_linked_list import Node, tail_to_head


def test_tail_to_head_moves_tail_to_front():
    daisy = Node("Daisy")
    mario = Node("Mario")
    toad = Node("Toad")
    peach = Node("Peach")
    daisy.next = mario
    mario.next = toad
    toad.next = peach

    result = tail_to_head(daisy)

    assert result.value == "Peach"
    assert result.next.value == "Daisy"
    assert result.next.next.value == "Mario"
    assert result.next.next.next.value == "Toad"


def test_tail_to_head_single_node():
    single = Node("Only")
    assert tail_to_head(single) is single
