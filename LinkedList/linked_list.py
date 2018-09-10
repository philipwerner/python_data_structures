"""LinkedList class module."""
from node import Node


class LinkedList(object):
    """LinkedList class."""

    def __init__(self, input=None):
        """Initializing the LinkedList object."""
        self.head = None
        self.length = 0
        if isinstance(input, (list, tuple)):
            for item in input:
                self.add(item)

    def __len__(self):
        """Magic method for returning length of LinkedList."""
        return self.length

    def add(self, input):
        """Add a node to the front of the Linked List."""
        new_node = Node(input)
        if self.head is None:
            self.head = new_node
            self.length += 1
        else:
            new_node._next = self.head
            self.head = new_node
            self.length += 1

    def append(self, input):
        """Add a new node to the LinkedList."""
        new_node = Node(input)
        if self.head is None:
            self.head = new_node
            self.length += 1
        else:
            current = self.front
            while current is not None:
                if current._next is None:
                    current._next = new_node
                    self.length += 1
                else:
                    current = current._next

    def pop(self):
        """Remove the first node in the Linked List."""
        if self.front is None:
            print("Linked List has no nodes to pop")
        else:
            temp = self.front
            self.front = temp._next
            temp._next = None
            self.length -= 1
            return temp.value
