from q1_building_a_playlist import top_hits_2010s


def test_playlist_contains_songs_in_order():
    assert top_hits_2010s is not None

    songs = []
    current = top_hits_2010s
    while current:
        songs.append(current.song)
        current = current.next

    assert songs == ["Uptown Funk", "Party Rock Anthem", "Bad Romance"]
