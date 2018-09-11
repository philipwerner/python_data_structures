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
            current = self.head
            while current is not None:
                if current._next is None:
                    current._next = new_node
                    self.length += 1
                    return
                else:
                    current = current._next

    def pop(self):
        """Remove the first node in the Linked List."""
        if self.head is None:
            return "Linked List has no nodes to pop"
        else:
            temp = self.head
            self.head = temp._next
            temp._next = None
            self.length -= 1
            return temp.value

    def add_before(self, input, target):
        """Add a node before a existing node in the LinkedList."""
        current = self.head
        previous = None
        new_node = Node(input)
        if target == self.head.value:
            new_node._next = self.head
            self.head = new_node
            self.length += 1
            return
        while current:
            if current.value != target:
                previous = current
                current = current._next
            elif current.value == target:
                new_node._next = current
                previous._next = new_node
                self.length += 1
                return

    def add_after(self, input, target):
        """Add a new node after a target node."""
        current = self.head
        new_node = Node(input)
        if target == self.head.value:
            new_node._next = self.head._next
            self.head._next = new_node
            self.length += 1
        else:
            while current:
                if current.value != target:
                    current = current._next
                elif current.value == target:
                    new_node._next = current._next
                    current._next = new_node
                    self.length += 1
                    return

    def find_node(self, input):
        """Check if node is in linked list."""
        current = self.head
        if self.head.value == input:
            return True
        else:
            while current:
                if current.value == input:
                    return True
                elif current.value != input:
                    current = current._next
        return False
