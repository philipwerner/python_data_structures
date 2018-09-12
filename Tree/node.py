"""Node class module for Binary Tree."""


class Node(object):
    """The Node class."""

    def __init__(self, value):
        """Initialization of node object."""
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        """Return a string representation of the node object."""
        return f'{self.value}'

    def __repr__(self):
        """Return a representation of the node object."""
        return f'<Node | Value: {self.value} | Left: {self.left} | Right: {self.right}>'
