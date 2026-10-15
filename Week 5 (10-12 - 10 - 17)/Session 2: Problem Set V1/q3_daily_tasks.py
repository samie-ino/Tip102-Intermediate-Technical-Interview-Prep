# Problem 3: Daily Tasks
# Imagine a linked list used as a daily task list where each node represents a task.
# Write a function add_first() that takes in the head of a linked list and adds a new node to the
# front of the task list.


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


def add_first(head, task):
    pass
