class Node:
    def __init__(self, key=None):
        self.val = key
        self.left = None
        self.right = None
        self.level_order_traversal = []

    def level_order(self, root):
        if not root:
            return

        queue = []
        queue.append(root)

        while queue:
            node = queue.pop(0)
            self.level_order_traversal.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    obj = Node()
    obj.level_order(root)
    print(obj.level_order_traversal)


main()
