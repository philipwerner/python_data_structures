"""Node Class for LinkedList module."""


class Node(object):
    """Node class for LinkedList."""

    def __init__(self, value):
        """Initialization of node object."""
        self.value = value
        self._next = None

    def __str__(self):
        """Return a formatted string representation on node."""
        return f'{self.value}'

    def __repr__(self):
        """Return a representation of the node."""
        return f'<Node | Value: {self.value} | Next : {self._next}>'
