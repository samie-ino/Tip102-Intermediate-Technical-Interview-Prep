'''
Problem 3: Daily Tasks
Imagine a linked list used as a daily task list where each node represents a task.
Write a function add_first() that takes in the head of a linked list and adds a new node to the
front of the task list.

UPI Plan

UNDERSTAND:
Input - The current head of the task list 
Output - The new head of the list, which is the node for the added task
Edge Cases - 


PLAN:
- Create a new node containing the new task 
- Set the new node's .next to the current head 
- Return the new node, because now its the front of the list



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
    
task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))
