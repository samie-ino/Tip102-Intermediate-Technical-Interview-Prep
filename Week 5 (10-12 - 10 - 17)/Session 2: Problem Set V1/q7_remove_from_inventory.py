# Problem 7: Remove From Inventory
# Imagine a linked list used to store a player's inventory. Write a function delete_item() that takes
# in the head of a linked list and a value item as parameters.
# The function should remove the first node it finds in the linked list with the value item and return
# the head of the modified list. If no node can be found with the value item, return the list unchanged.


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


def delete_item(head, item):
    pass
