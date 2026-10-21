from q5_looped import SongNode, loop_length


def test_loop_length_counts_cycle_nodes():
    song1 = SongNode("Wein", "AL SHAMI")
    song2 = SongNode("Si Ai", "Tayna")
    song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
    song4 = SongNode("La", "DYSTINCT")
    song1.next = song2
    song2.next = song3
    song3.next = song4
    song4.next = song2

    assert loop_length(song1) == 3


def test_loop_length_returns_zero_without_cycle():
    playlist = SongNode("Wein", "AL SHAMI", SongNode("Si Ai", "Tayna"))

    assert loop_length(playlist) == 0


def test_loop_length_returns_zero_for_empty_playlist():
    assert loop_length(None) == 0
