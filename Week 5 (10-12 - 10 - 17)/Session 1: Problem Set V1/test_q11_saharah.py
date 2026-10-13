from q11_saharah import saharah, timmy, tom_nook, tommy


def test_list_relinks_without_tom_nook():
    assert tom_nook.next is None
    assert timmy.value == "Timmy"
    assert timmy.next is tommy
    assert tommy.value == "Tommy"
    assert tommy.next is saharah
    assert saharah.value == "Saharah"
    assert saharah.next is None