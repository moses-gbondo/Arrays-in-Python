class Node:
    def __init__(self, data):
        self.next = None
        self.val = data

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse_list(self):
        temp = self.head
        while temp != None:
            print(temp.val)
            temp = temp.next

    def reverse_list(self):
        current = self.head
        prev = None
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def length_of_list(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return(count)

def main():
    llist = LinkedList()
    llist.insert_node(1)
    llist.insert_node(2)
    llist.insert_node(3)
    llist.insert_node(4)
    llist.insert_node(5)
    llist.length_of_list()
    llist.traverse_list()
    llist.reverse_list()
    llist.traverse_list()
main()
