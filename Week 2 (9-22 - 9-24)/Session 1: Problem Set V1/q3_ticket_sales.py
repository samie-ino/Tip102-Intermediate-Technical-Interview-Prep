# Problem 3: Ticket Sales
# A venue tracks how many tickets are sold for each show.
# Write a function ticket_sales(sales) that totals the tickets sold.
#
# def ticket_sales(sales):
#     pass
#
# Example Usage:
#
# sales = {"Friday": 120, "Saturday": 200}
# print(ticket_sales(sales))
#
# Example Output:
#
# 320



"""
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
