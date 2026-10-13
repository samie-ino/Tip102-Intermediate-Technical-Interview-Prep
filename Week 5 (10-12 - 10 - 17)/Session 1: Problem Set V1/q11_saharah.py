# Problem 11: Saharah
# Detach Tom Nook and link Saharah after Tommy.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


tommy = Node("Tommy")
timmy = Node("Timmy", tommy)
tom_nook = Node("Tom Nook", timmy)
saharah = Node("Saharah")
tom_nook.next = None
tommy.next = saharah


if __name__ == "__main__":
    print(tom_nook.next)
    print(timmy.value)
    print(timmy.next.value)
    print(tommy.value)
    print(tommy.next.value)
    print(saharah.value)
    print(saharah.next)