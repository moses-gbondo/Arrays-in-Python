class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.val)
            temp = temp.next

    def push(self, data):
        # The new node is added before the head of the given Linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self,data, prev):
        if prev == None:
            print("The given prev node cannot be none")
            return

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def append(self, data):
        current = self.head
        temp = None
        new_node =  Node(data)
        while current != None:
            temp = current
            current = current.next
        temp.next = new_node


def main():
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = None
    llist.print_list()
    push_obj = LinkedList()
    push_obj.push('a')
    push_obj.push('b')
    push_obj.push('c')
    push_obj.push('d')
    push_obj.push('e')
    push_obj.print_list()
    push_obj.append('u')
    push_obj.append('v')
    push_obj.append('w')
    push_obj.append('x')
    push_obj.print_list()


main()
