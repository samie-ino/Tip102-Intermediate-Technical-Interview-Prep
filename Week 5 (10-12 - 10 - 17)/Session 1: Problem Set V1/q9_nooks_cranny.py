# Problem 9: Nook's Cranny
# Create and link Tom Nook to Tommy using Node instances.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


tom_nook = Node("Tom Nook")
tommy = Node("Tommy")
tom_nook.next = tommy


if __name__ == "__main__":
    print(tom_nook.value)
    print(tom_nook.next.value)
    print(tommy.value)
    print(tommy.next)