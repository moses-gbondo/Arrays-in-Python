
class Tree:
    def __init__(self, key=None):
        self.data = key
        self.left = None
        self.right = None

    def print_given_level(self, root, level):
        if level == 0:
            return
        if level == 1:
            print(root.data)
        elif level > 1:
            self.print_given_level(root.right, level - 1)
            self.print_given_level(root.left, level - 1)

    def height(self, root):
        if root is None:
            return 0
        else:
            lheight = self.height(root.left)
            rheight = self.height(root.right)
            if lheight > rheight:
                return rheight + 1
            else:
                return lheight + 1

    def print_level_order(self, root):
        h = self.height(root)
        for i in range(h, 0, -1):
            self.print_given_level(root, i)


def main():
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.right.left = Tree(6)
    root.right.right = Tree(7)
    obj = Tree()
    obj.print_level_order(root)


main()
