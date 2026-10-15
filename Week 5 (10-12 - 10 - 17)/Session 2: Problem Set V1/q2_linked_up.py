# Problem 2: Linked Up
# Connect the provided node instances below to create the linked list:
# K.K. Slider -> Harriet -> Saharah -> Isabelle


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


kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# Add code here to link the above nodes
