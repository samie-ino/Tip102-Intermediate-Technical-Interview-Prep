'''
Problem 4: Halve List
Write a function halve_list() that accepts the head of a linked list whose values are integers
and divides each value by two. Return the head of the modified list.


UPI Plan

UNDERSTAND:
Input - The head of a linked list whose node values are integers.
Output - The head of the modified list, with each value divided by two.
Edge Cases - 
-If the list is empty (head is None), return None.
-If the list has one node, update that value and return the same head.
-Integer values can be odd, so dividing by two may produce a float (for example, 5 / 2 is 2.5 in Python).

PLAN:
- Set a pointer, such as current, to head.
- While current is not None:
- Divide current.value by two and store the result back in current.value.
- Move current to the next node.
- Return head. The node links stay the same; only the values change.

IMPLEMENT:
- Code Below!

'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def add_first(head, task):
    new_node = Node(task)
    new_node.next = head
    return new_node

def halve_list(head):
    current = head
    while current:
        current.value = current.value / 2
        current = current.next
    return head
    
node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))
