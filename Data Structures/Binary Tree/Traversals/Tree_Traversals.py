class Node:
    def __init__(self, key=None):
        self.val = key
        self.left = None
        self.right = None
        self.inorder_array = []
        self.preorder_array = []
        self.postorder_array = []

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorder_array.append(root.val)
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            self.preorder_array.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)


    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.postorder_array.append(root.val)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    obj = Node()
    obj.inorder(root)
    obj.preorder(root)
    obj.postorder(root)
    print("Inorder ", obj.inorder_array)
    print("Postorder ", obj.postorder_array)
    print("Preorder ", obj.preorder_array)
main()
