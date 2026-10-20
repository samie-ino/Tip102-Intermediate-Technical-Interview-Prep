from q3_glitching_out import SongNode, remove_song


def test_remove_song_from_middle_of_playlist():
    playlist = SongNode(
        "SOS",
        "ABBA",
        SongNode(
            "Simple Twist of Fate",
            "Bob Dylan",
            SongNode("Dreams", "Fleetwood Mac", SongNode("Lovely Day", "Bill Withers")),
        ),
    )

    result = remove_song(playlist, "Dreams")
    songs = []
    current = result
    while current:
        songs.append(current.song)
        current = current.next

    assert songs == ["SOS", "Simple Twist of Fate", "Lovely Day"]


def test_remove_song_from_head():
    playlist = SongNode("SOS", "ABBA", SongNode("Dreams", "Fleetwood Mac"))

    result = remove_song(playlist, "SOS")

    assert result.song == "Dreams"


def test_remove_song_from_empty_playlist():
    assert remove_song(None, "Dreams") is None
