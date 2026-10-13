# Problem 10: Timmy and Tommy
# Place Timmy between Tom Nook and Tommy in the linked list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


tommy = Node("Tommy")
timmy = Node("Timmy", tommy)
tom_nook = Node("Tom Nook", timmy)


if __name__ == "__main__":
    print(tom_nook.value)
    print(tom_nook.next.value)
    print(timmy.value)
    print(timmy.next.value)
    print(tommy.value)
    print(tommy.next)