# Edge case: blank or empty note lists should return an empty result cleanly.

from q8_event_notes import event_notes


def test_event_notes_basic():
    items = ["check-in", "setup", "rehearsal"]
    assert event_notes(items) == ["check-in", "setup", "rehearsal"]


def test_event_notes_empty():
    assert event_notes([]) == []
