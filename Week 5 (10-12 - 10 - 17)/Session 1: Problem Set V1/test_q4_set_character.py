from q4_set_character import Villager


def test_valid_catchphrase_updates_value(capsys):
    villager = Villager("Alice", "Koala", "guvnor")
    villager.set_catchphrase("sweet dreams")
    assert villager.catchphrase == "sweet dreams"
    assert capsys.readouterr().out.strip() == "Catchphrase updated"


def test_invalid_catchphrase_keeps_old_value(capsys):
    villager = Villager("Alice", "Koala", "guvnor")
    villager.set_catchphrase("#?!")
    assert villager.catchphrase == "guvnor"
    assert capsys.readouterr().out.strip() == "Invalid catchphrase"


def test_catchphrase_must_be_shorter_than_twenty_characters(capsys):
    villager = Villager("Alice", "Koala", "guvnor")
    villager.set_catchphrase("a" * 20)
    assert villager.catchphrase == "guvnor"
    assert capsys.readouterr().out.strip() == "Invalid catchphrase"