'''
In a linked list, pointers can be redirected to any place in the list.

Using the linked list from Problem 9, create a new Node timmy with value 
"Timmy" and place it between tom_nook and tommy so the new linked list is 
tom_nook -> timmy -> tommy.

'''


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