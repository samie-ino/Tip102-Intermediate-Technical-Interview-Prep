# Problem 6: Find Minimum in Linked List
# Write a function find_min() that takes in the head of a linked list and returns the minimum
# value in the linked list. You can assume the linked list will contain only numeric values.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "
")
        current = current.next


def find_min(head):
    pass
