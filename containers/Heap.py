from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    def __init__(self, xs=None):
        super().__init__()
        self.num_nodes = 0
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        ret = True
        if node.left:
            ret &= node.value <= node.left.value
            ret &= Heap._is_heap_satisfied(node.left)
        if node.right:
            ret &= node.value <= node.right.value
            ret &= Heap._is_heap_satisfied(node.right)
        return ret

    def insert(self, value):
        '''
        '''
        self.num_nodes += 1
        binary_str = str(bin(self.num_nodes))[3:]

        if self.root is None:
            self.root = Node(value)
        else:
            Heap._insert(self.root, value, binary_str)

    @staticmethod
    def _insert(node, value, binary_str):
        if not binary_str:
            node = Node(value)
        elif binary_str[0] == '0':
            if len(binary_str) == 1:
                node.left = Node(value)
            else:
                Heap._insert(node.left, value, binary_str[1:])
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
        elif binary_str[0] == '1':
            if len(binary_str) == 1:
                node.right = Node(value)
            else:
                Heap._insert(node.right, value, binary_str[1:])
            if node.value > node.right.value:
                node.value, node.right.value = node.right.value, node.value

    def insert_list(self, xs):
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        return self.root.value

    def remove_min(self):
        binary_str = str(bin(self.num_nodes))[3:]
        bottom = Heap._remove_bottom(self.root, binary_str)
        self.num_nodes -= 1
        self.root.value = bottom
        Heap._trickle_down(self.root)

    @staticmethod
    def _remove_bottom(node, binary_str):
        if node.left:
            if binary_str[0] == '0':
                if len(binary_str) == 1:
                    bottom = node.left.value
                    node.left = None
                else:
                    bottom = Heap._remove_bottom(node.left, binary_str[1:])
            if binary_str[0] == '1':
                if len(binary_str) == 1:
                    bottom = node.right.value
                    node.right = None
                else:
                    bottom = Heap._remove_bottom(node.right, binary_str[1:])
            return bottom

    @staticmethod
    def _trickle_down(node):
        if node.left and node.right:
            if node.value > node.left.value < node.right.value:
                node.value, node.left.value = node.left.value, node.value
                Heap._trickle_down(node.left)
            if node.value > node.right.value < node.left.value:
                node.value, node.right.value = node.right.value, node.value
                Heap._trickle_down(node.right)
        if node.left:
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
                Heap._trickle_down(node.left)
