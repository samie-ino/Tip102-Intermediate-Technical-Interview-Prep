'''
In a linked list, pointers can be redirected to any place in the list.

Using the linked list from Problem 9, create a new Node timmy with value 
"Timmy" and place it between tom_nook and tommy so the new linked list is 
tom_nook -> timmy -> tommy.

UPI Plan 

UNDERSTAND:
Input - 
OUtput - 
Edge Cases -

PLAN:


IMPLEMENT: 
- (implemented below)

'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
