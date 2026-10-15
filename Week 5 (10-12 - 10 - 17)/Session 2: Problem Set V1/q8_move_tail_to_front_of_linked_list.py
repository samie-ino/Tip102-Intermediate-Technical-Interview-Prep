# Problem 8: Move Tail to Front of Linked List
# Write a function tail_to_head() that takes in the head of a linked list as a parameter and
# moves the tail of the linked list to the front.


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


def tail_to_head(head):
    pass
