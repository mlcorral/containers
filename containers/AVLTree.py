from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    def __init__(self, xs=None):
        super().__init__()

    def balance_factor(self):
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        elif not node:
            return True
        else:
            left_satisfied = AVLTree._is_avl_satisfied(node.left)
            right_satisfied = AVLTree._is_avl_satisfied(node.right)
            return left_satisfied and right_satisfied

    @staticmethod
    def _left_rotate(node):
        old_root = node
        if old_root.right:
            new_root = Node(old_root.right.value)
            new_root.left = Node(old_root.value)
            new_root.right = old_root.right.right
            new_root.left.left = old_root.left
            new_root.left.right = old_root.right.left
            return new_root
        return old_root

    @staticmethod
    def _right_rotate(node):
        old_root = node
        if old_root.left:
            new_root = Node(old_root.left.value)
            new_root.right = Node(old_root.value)
            new_root.left = old_root.left.left
            new_root.right.right = old_root.right
            new_root.right.left = old_root.left.right
            return new_root
        return old_root

    def insert(self, value):
        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    def insert_list(self, xs):
        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _insert(node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        if AVLTree._balance_factor(node) > 1:
            if value < node.left.value:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        if AVLTree._balance_factor(node) < -1:
            if value > node.right.value:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        return node

