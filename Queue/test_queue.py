"""Test module for Queue class."""
from queue import Queue
import pytest


@pytest.fixture
def empty_queue():
    """Create an empty Queue."""
    return Queue()


@pytest.fixture
def filled_queue():
    """Create a queue with data."""
    return Queue([1, 2, 3, 4, 5, 6])


def test_can_instantiate_a_queue():
    """Test a Queue object can be made."""
    q = Queue()
    assert isinstance(q, Queue)


def test_len_method_shows_length_when_enqueue_into_empty_queue(empty_queue):
    """Test proper length is return when equeue into empty queue."""
    empty_queue.enqueue(12)
    actual = len(empty_queue)
    assert actual == 1


def test_can_instantiate_a_queue_with_iter():
    """Test can create a queue with a iterable."""
    q = Queue([1, 2, 3, 4, 5, 6])
    assert len(q) == 6


def test_can_enqueue_into_empty_queue(empty_queue):
    """Test that enqueue adds node to queue."""
    empty_queue.enqueue(9)
    assert empty_queue.front.value == 9


def test_can_enqueue_multiple_times(empty_queue):
    """Test that no error occurs when multiple enqueues happen."""
    for x in range(20):
        empty_queue.enqueue(x)
    assert len(empty_queue) == 20


def test_len_on_iterable_created_queue(filled_queue):
    """Test the len method works on iterable filled queue."""
    actual = len(filled_queue)
    assert actual == 6


def test_can_dequeue_from_iter_created_queue(filled_queue):
    """Test that dequeue works on iterable created queue."""
    start_length = len(filled_queue)
    filled_queue.dequeue()
    assert start_length > len(filled_queue)
    assert len(filled_queue) == 5


def test_peek_shows_right_value(filled_queue):
    """Test that the front value is shown when peek is called."""
    assert filled_queue.peek() == 1


def test_peek_shows_right_value_after_dequeue(filled_queue):
    """Test that the new front is shown on peek after a dequeue."""
    filled_queue.dequeue()
    assert filled_queue.peek() == 2


def test_that_rear_is_the_right_value_at_length_of_one(empty_queue):
    """Test that rear is the same as front at length of 1."""
    empty_queue.enqueue(9)
    assert empty_queue.front == empty_queue.rear


def test_that_rear_is_the_right_value_at_length_greater_than_one(empty_queue):
    """Test that rear is the same as front at length of 1."""
    empty_queue.enqueue(9)
    empty_queue.enqueue(1)
    assert empty_queue.front.value == 9
    assert empty_queue.rear.value == 1
