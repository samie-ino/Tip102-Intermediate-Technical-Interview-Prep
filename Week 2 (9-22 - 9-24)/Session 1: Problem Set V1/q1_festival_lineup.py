# Problem 1: Festival Lineup
# A festival organizer wants to order the performers in a way that looks good on stage.
# Write a function festival_lineup(performers) that returns the performers in the desired order.
#
# def festival_lineup(performers):
#     pass
#
# Example Usage:
#
# performers = ["Milo", "Juno", "Luna"]
# print(festival_lineup(performers))
#
# Example Output:
#
# ["Milo", "Juno", "Luna"]


"""
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
