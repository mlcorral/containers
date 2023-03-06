from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):

    def __init__(self, xs=None):
        super().__init__()
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def __eq__(self, t2):
        sorted_list1 = self.to_list('inorder')
        sorted_list2 = t2.to_list('inorder')
        return sorted_list1 == sorted_list2

    def is_bst_satisfied(self):
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        ret = True
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        if self.root:
            BST._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
        if value <= node.value:
            if node.left:
                BST._insert(node.left, value)
            else:
                node.left = Node(value)
        if value >= node.value:
            if node.right:
                BST._insert(node.right, value)
            else:
                node.right = Node(value)

    def insert_list(self, xs):
        for x in xs:
            if self.root:
                BST._insert(self.root, x)
            else:
                self.root = Node(x)

    def __contains__(self, value):
        return self.find(value)

    def find(self, value):
        if not self.root:
            return None
        else:
            return BST._find(value, self.root)

    @staticmethod
    def _find(value, node):
        if value == node.value:
            return True
        if value < node.value:
            if node.left:
                return BST._find(value, node.left)
            else:
                return False
        if value > node.value:
            if node.right:
                return BST._find(value, node.right)
            else:
                return False

