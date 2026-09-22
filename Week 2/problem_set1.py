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

