from q4_on_repeat import SongNode, on_repeat


def test_on_repeat_detects_cycle():
    song1 = SongNode("GO!", "Common")
    song2 = SongNode("N95", "Kendrick Lamar")
    song3 = SongNode("WIN", "Jay Rock")
    song4 = SongNode("ATM", "J. Cole")
    song1.next = song2
    song2.next = song3
    song3.next = song4
    song4.next = song2

    assert on_repeat(song1) is True


def test_on_repeat_returns_false_for_acyclic_playlist():
    playlist = SongNode("GO!", "Common", SongNode("N95", "Kendrick Lamar"))

    assert on_repeat(playlist) is False


def test_on_repeat_returns_false_for_empty_playlist():
    assert on_repeat(None) is False
