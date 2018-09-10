"""Queue class module."""
from node import Node


class Queue(object):
    """The Queue class."""

    def __init__(self, input=None):
        """Initializing the Queue object."""
        self.front = None
        self.rear = None
        self.length = 0
        if isinstance(input, (list, tuple)):
            for item in input:
                self.enqueue(item)

    def __len__(self):
        """Magic method to return length of Queue."""
        return self.length

    def enqueue(self, input):
        """Add a new node to the rear of the queue."""
        new_node = Node(input)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            self.length += 1
            return
        else:
            temp = self.rear
            self.rear = new_node
            temp._next = self.rear
            self.length += 1
            return

    def dequeue(self):
        """Remove the node at the front of the queue."""
        if self.front is None:
            print('There is nothing to dequeue.')
        elif self.front._next is None:
            temp = self.front
            self.front = None
            self.length -= 1
            return temp.value
        else:
            temp = self.front
            self.front = temp._next
            temp._next = None
            self.length -= 1
            return temp.value

    def peek(self):
        """Will show the node value at the front of the queue."""
        return self.front.value
