from problem4_engagement_boost import engagement_boost

def test_engagement_boost():
    assert engagement_boost([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert engagement_boost([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]