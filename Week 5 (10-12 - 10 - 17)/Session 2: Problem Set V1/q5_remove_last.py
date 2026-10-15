# Problem 5: Remove Last
# Write a function delete_tail() that accepts the head of a linked list and removes the last node.
# Return the head of the modified list.


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


def delete_tail(head):
    pass
