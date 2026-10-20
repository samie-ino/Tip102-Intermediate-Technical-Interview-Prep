from q2_top_artists import SongNode, get_artist_frequency


def test_get_artist_frequency_counts_repeated_artists():
    playlist = SongNode(
        "Saturn",
        "SZA",
        SongNode(
            "Who",
            "Jimin",
            SongNode("Espresso", "Sabrina Carpenter", SongNode("Snooze", "SZA")),
        ),
    )

    assert get_artist_frequency(playlist) == {
        "SZA": 2,
        "Jimin": 1,
        "Sabrina Carpenter": 1,
    }


def test_get_artist_frequency_empty_playlist():
    assert get_artist_frequency(None) == {}
