from q6_strongest_avenger import strongest_avenger


def test_strongest_avenger_examples():
    assert strongest_avenger([88, 92, 95, 99, 97, 100, 94]) == 100
    assert strongest_avenger([50, 75, 85, 60, 90]) == 90
