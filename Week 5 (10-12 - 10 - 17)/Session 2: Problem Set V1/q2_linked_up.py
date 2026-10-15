'''
Problem 2: Linked Up
Connect the provided node instances below to create the linked list:
K.K. Slider -> Harriet -> Saharah -> Isabelle

UPI Plan

UNDERSTAND:
Input - Four Existing Nodes
Output - Create a linked list with the nodes
Edge Cases - 
- Isabelle has to be equal to None

PLAN:
- Set K.K Slider .next to Harriet 
- Set Harriet's .next to Saharah 
- Set Saharah's .next to Isabelle
- Make sure Isabelle's .next is None
- Call printed_linked_list(kk_slider) to check the requested order


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



kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# Add code here to link the above nodes
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle
              
print_linked_list(kk_slider)