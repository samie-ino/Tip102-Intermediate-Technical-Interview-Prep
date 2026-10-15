import io
from contextlib import redirect_stdout

from q10_print_backwards import Node, print_reverse


def test_print_reverse_prints_values_in_reverse_order():
    isabelle = Node("Isabelle")
    kk_slider = Node("K.K. Slider")
    saharah = Node("Saharah")
    isabelle.next = kk_slider
    kk_slider.next = saharah
    saharah.prev = kk_slider
    kk_slider.prev = isabelle

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        print_reverse(saharah)

    assert buffer.getvalue().strip() == "Saharah K.K. Slider Isabelle"
