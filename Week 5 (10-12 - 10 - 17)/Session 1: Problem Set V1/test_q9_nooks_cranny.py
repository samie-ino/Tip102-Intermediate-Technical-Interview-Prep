from q9_nooks_cranny import tom_nook, tommy


def test_tom_nook_points_to_tommy():
    assert tom_nook.value == "Tom Nook"
    assert tom_nook.next is tommy
    assert tommy.value == "Tommy"
    assert tommy.next is None