from q6_volume_control import Node, count_critical_points


def test_count_critical_points_counts_local_minima_and_maxima():
    song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

    assert count_critical_points(song_audio) == 3


def test_count_critical_points_ignores_head_and_tail():
    song_audio = Node(1, Node(3, Node(2)))

    assert count_critical_points(song_audio) == 1


def test_count_critical_points_short_or_empty_list():
    assert count_critical_points(None) == 0
    assert count_critical_points(Node(1, Node(2))) == 0
