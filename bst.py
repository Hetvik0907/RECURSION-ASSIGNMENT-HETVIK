class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def print(self):
        self.print_leaf_nodes1(self.root)

    def print_leaf_nodes1(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.key, end=" ")
        self.print_leaf_nodes1(node.left)
        self.print_leaf_nodes1(node.right)

bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
bst.print()