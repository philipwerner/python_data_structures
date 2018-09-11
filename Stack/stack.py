"""Stack class module."""
from node import Node


class Stack(object):
    """The Stack class."""

    def __init__(self, input=None):
        """Initializing the Stack."""
        self.top = None
        self.height = 0
        if isinstance(input, (list, tuple)):
            for item in input:
                self.add(item)

    def add(self, value):
        """Add a node to the stack."""
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.height += 1
        else:
            temp = self.top
            self.top = new_node
            new_node._next = temp
            self.height += 1

    def pop(self):
        """Remove top node from stack."""
        if self.top is None:
            return 'The stack is empty'
        else:
            temp = self.top
            self.top = temp._next
            temp._next = None
            self.height -= 1
            return temp.value

    def peek(self):
        """Show the value of the node at the top of the stack."""
        return self.top.value

    def height(self):
        """Return the height of the stack."""
        return self.height
