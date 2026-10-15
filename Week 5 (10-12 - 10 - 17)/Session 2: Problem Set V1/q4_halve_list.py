# Problem 4: Halve List
# Write a function halve_list() that accepts the head of a linked list whose values are integers
# and divides each value by two. Return the head of the modified list.


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


def halve_list(head):
    pass
