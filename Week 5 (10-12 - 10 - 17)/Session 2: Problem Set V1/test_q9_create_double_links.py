from q9_create_double_links import head, tail


def test_double_linked_list_has_prev_and_next_links():
    assert head.value == "Isabelle"
    assert tail.value == "K.K. Slider"
    assert head.next is tail
    assert tail.prev is head
    assert head.prev is None
    assert tail.next is None
