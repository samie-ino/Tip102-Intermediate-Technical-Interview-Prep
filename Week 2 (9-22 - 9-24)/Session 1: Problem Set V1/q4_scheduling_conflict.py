# Problem 4: Scheduling Conflict
# A scheduler checks whether two events overlap in time.
# Write a function scheduling_conflict(start1, end1, start2, end2) that returns True if there is a conflict.
#
# def scheduling_conflict(start1, end1, start2, end2):
#     pass
#
# Example Usage:
#
# print(scheduling_conflict(1, 5, 3, 7))
#
# Example Output:
#
# True


"""
Problem 4
    UNDERSTAND:
    Input: two dictionaries mapping artist names to set times
    Output: dictionary containing artists with the same set time at both venues
    Edge Cases:
    - empty dictionaries -> return an empty dictionary
    - artists appearing in only one schedule are not conflicts
    - artists with different set times are not conflicts

    PLAN:
    - create a dictionary called conflicts
    - loop through the artists in venue1_schedule
    - check if the artist is also in venue2_schedule
    - check if both set times are the same
    - add matching artists and times to conflicts
    - return conflicts

IMPLEMENT: (below)
"""


def find_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {}

    for artist in venue1_schedule:
        if (
            artist in venue2_schedule
            and venue1_schedule[artist] == venue2_schedule[artist]
        ):
            conflicts[artist] = venue1_schedule[artist]

    return conflicts
