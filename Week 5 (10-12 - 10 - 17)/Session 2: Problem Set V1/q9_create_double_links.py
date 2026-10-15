# Problem 9: Create Double Links
# One of the drawbacks of a linked list is that it's difficult to go backwards because each Node only
# knows about the Node in front of it.
# A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked
# list also has a prev attribute that points to the Node before it.
# Update the Node constructor below so that the code creates a doubly linked list with
# head <-> tail.


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


head = Node("Isabelle")
tail = Node("K.K. Slider")
