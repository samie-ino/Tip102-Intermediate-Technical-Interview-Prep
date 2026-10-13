from q3_update_catchphrase import bones


def test_bones_catchphrase_updated():
    assert bones.catchphrase == "ruff it up"


def test_greeting_uses_updated_catchphrase():
    assert bones.greet_player("Samia") == (
        "Bones: Hey there, Samia! How's it going, ruff it up!"
    )