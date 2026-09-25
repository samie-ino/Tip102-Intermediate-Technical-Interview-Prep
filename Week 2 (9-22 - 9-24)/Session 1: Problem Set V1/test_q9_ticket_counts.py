# Edge case: zero-ticket entries should not affect the total.

from q9_ticket_counts import ticket_counts


def test_ticket_counts_basic():
    tickets = {"VIP": 20, "General": 40}
    assert ticket_counts(tickets) == 60


def test_ticket_counts_empty():
    assert ticket_counts({}) == 0
