"""Binary Tree class module."""
from node import Node


class BinaryTree(object):
    """Binary Tree class."""

    def __init__(self, input=None):
        """Initializer for the binary tree object."""
        self.root = None
        self._count = 0
        if isinstance(input, (list, tuple)):
            for item in input:
                self.add(item)

    def add(self, input):
        """Add a node to the binary tree."""
        if self.root is None:
            self.root = Node(input)
            self._count += 1
            return

        curr = self.root
        while curr:
            if input == curr.value:
                raise ValueError('Node already exists')
            elif input < curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(input)
                    self._count += 1
                    break
            elif input > curr.value:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(input)
                    self._count += 1
                    break

    def in_order(self, callable=lambda node: print(node)):
        """Go left, visit, then go right."""
        def _walk(node=None):
            if node is None:
                return
            if node.left:
                _walk(node.left)
            callable(node)
            if node.right:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node)):
        """Visit, go left, then right."""
        def _walk(node=None):
            if node is None:
                return
            callable(node)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
        """Go left, then right, Visit."""
        def _walk(node=None):
            if node is None:
                return
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            callable(node)
        _walk(self.root)
