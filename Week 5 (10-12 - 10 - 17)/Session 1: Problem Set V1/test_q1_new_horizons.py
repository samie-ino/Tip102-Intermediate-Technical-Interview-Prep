from q1_new_horizons import apollo


def test_apollo_attributes():
    assert apollo.name == "Apollo"
    assert apollo.species == "Eagle"
    assert apollo.catchphrase == "pah"
    assert apollo.furniture == []