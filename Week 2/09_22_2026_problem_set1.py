"""
Problem 1
UNDERSTAND:
Input: 2 lists of strings: artists and set_times
Output: dictionary mapping artist names to set time
Edge Cases:
- 

PLAN:
- Have an empty dictionary to store the mapping
- for loop through in the range of the length of the artists list
- for each index, add the artist name as the key and its set time
- Then return the dictionary

IMPLEMENT: (below)
"""


def lineup(artists, set_times):
    lineup = {}

    for i in range(len(artists)):
        lineup[artists[i]] = set_times[i]
    return lineup


"""
Problem 2
UNDERSTAND:
Input: dictionary mapping ticket type to number of tickets sold
Output: integer representing all tickets sold
Edge Cases:
- if tickets sold is negative -> 0
- empty dictionary -> return 0

PLAN:
- create a variable count to store number of tickets
- loop through the keys in ticket_sales
- for each ticket type, add that total to count
- return count

IMPLEMENT: (below)
"""


def total_sales(ticket_sales):
    count = 0

    for value in ticket_sales.values():
        count += value
    return count

"""
Problem 3
    UNDERSTAND:
    Input: dictionary mapping ticket types to tickets sold
    Output: integer representing the total tickets sold
    Edge Cases:
    - negative ticket amounts count as 0
    - empty dictionary -> return 0

    PLAN:
    - create a variable count to store the total tickets
    - loop through the ticket types in ticket_sales
    - get the number of tickets sold
    - add it to count only if it is positive
    - return count

IMPLEMENT:
"""

def positive_sales(ticket_sales):
    count = 0

    for ticket_type in ticket_sales:
        tickets_sold = ticket_sales[ticket_type]

        if tickets_sold > 0:
            count += tickets_sold

    return count



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
