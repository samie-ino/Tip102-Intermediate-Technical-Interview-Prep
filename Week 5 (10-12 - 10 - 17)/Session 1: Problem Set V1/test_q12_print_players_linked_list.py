from q12_print_players_linked_list import Node, print_list


def test_print_list_values_with_arrow_separator():
    isabelle = Node("Isabelle")
    saharah = Node("Saharah")
    cj = Node("C.J.")
    isabelle.next = saharah
    saharah.next = cj
    assert print_list(isabelle) == "Isabelle -> Saharah -> C.J."


def test_print_single_node():
    assert print_list(Node("Isabelle")) == "Isabelle"