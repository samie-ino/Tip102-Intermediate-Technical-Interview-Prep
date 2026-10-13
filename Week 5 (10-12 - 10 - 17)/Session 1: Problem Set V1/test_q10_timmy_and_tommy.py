from q10_timmy_and_tommy import timmy, tom_nook, tommy


def test_timmy_is_between_tom_nook_and_tommy():
    assert tom_nook.value == "Tom Nook"
    assert tom_nook.next is timmy
    assert timmy.value == "Timmy"
    assert timmy.next is tommy
    assert tommy.value == "Tommy"
    assert tommy.next is None