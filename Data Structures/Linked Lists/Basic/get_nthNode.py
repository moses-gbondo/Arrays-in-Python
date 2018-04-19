#Write a function to get Nth node in a Linked List
#Write a GetNth() function that takes a linked list and an integer index and returns the data value stored in the node at that index position.

#Example:

#Input:  1->10->30->14,  index = 2
#Output: 30  
#The node at index 2 is 30


class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def get_nthNode(self, index):
        current = self.head
        if index == 0:
            print(current.val)
            return

        while index != 0:
            index -= 1
            current = current.next
        print(current.val)


def main():
    List = LinkedList()
    List.push_node(0)
    List.push_node(1)
    List.push_node(2)
    List.push_node(3)
    List.push_node(4)
    List.push_node(5)
    List.push_node(6)
    List.get_nthNode(2)
main()
