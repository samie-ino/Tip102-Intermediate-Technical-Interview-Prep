# Problem 12: Print Players Linked List
# Return the node values joined with " -> ".


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_list(head):
    pass


if __name__ == "__main__":
    isabelle = Node("Isabelle")
    saharah = Node("Saharah")
    cj = Node("C.J.")
    isabelle.next = saharah
    saharah.next = cj
    print(print_list(isabelle))