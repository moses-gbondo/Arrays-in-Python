/*
Write a C function that searches a given key ‘x’ in a given singly linked list. The function should return true if x is present in linked list and false otherwise.
*/
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

    def search_list(self, data):
        current = self.head

        while current != None:
            if current.val == data:
                return True
            current = current.next
        return False

def main():
    List = LinkedList()
    List.push_node(1)
    List.push_node(2)
    List.push_node(3)
    List.push_node(4)
    List.push_node(5)
    print(List.search_list(5))
    print(List.search_list(6))
main()
