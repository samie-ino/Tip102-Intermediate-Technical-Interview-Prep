from q8_telephone import Villager, message_received


def test_target_reachable_through_neighbors():
    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
    kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
    isabelle.neighbor = tom_nook
    tom_nook.neighbor = kk_slider
    assert message_received(isabelle, kk_slider) is True


def test_unreachable_target_returns_false():
    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
    assert message_received(kk_slider, isabelle) is False