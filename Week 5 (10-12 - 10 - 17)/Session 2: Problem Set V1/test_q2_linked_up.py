from q2_linked_up import kk_slider, harriet, saharah, isabelle


def test_linked_up_nodes_are_connected():
    assert kk_slider.value == "K.K. Slider"
    assert kk_slider.next is harriet
    assert harriet.next is saharah
    assert saharah.next is isabelle
    assert isabelle.next is None
