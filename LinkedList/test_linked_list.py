"""Testing module for Linked List clss."""
from linked_list import LinkedList
import pytest


@pytest.fixture
def empty_list():
    """Create empty LinkedList."""
    return LinkedList()


@pytest.fixture
def filled_list():
    """Create a populated LinkedList."""
    x = LinkedList([12, 34, 2, 67, 43, 98, 76])
    return x


def test_instatiating_a_linked_list():
    """Test that a linked list object can be created."""
    x = LinkedList()
    assert isinstance(x, LinkedList)


def test_instatiating_linked_list_with_iter():
    """Test that Linked List can be created with an iterable."""
    x = LinkedList([1, 2, 3, 4, 5, 6, 7])
    assert isinstance(x, LinkedList)


def test_length_method_works(empty_list):
    """Test that the length method works."""
    assert len(empty_list) == 0


def test_length_method_works_after_adding_one_node(empty_list):
    """Test that length works after adding node to empty list."""
    empty_list.add(9)
    assert len(empty_list) == 1


def test_length_works_after_multiple_adds(empty_list):
    """Test that length works after multiple nodes have been added."""
    for x in range(20):
        empty_list.add(x)
    assert len(empty_list) == 20


def test_find_node_works_while_node_exist(filled_list):
    """Test that find_node method works."""
    assert filled_list.find_node(67)


def test_find_node_works_while_node_does_not_exist(filled_list):
    """Test that find_node method works."""
    assert filled_list.find_node(999) is False


def test_pop_method_works(filled_list):
    """Test that pop method removes a node."""
    filled_list.pop()
    assert filled_list.find_node(7) is False


def test_length_is_reduced_after_pop(filled_list):
    """Test that the length is changed after a pop."""
    starting_length = len(filled_list)
    filled_list.pop()
    assert starting_length > len(filled_list)


def test_append_adds_to_end_of_list(empty_list):
    """Test that an appended node goes to the end of the list."""
    empty_list.add(1)
    empty_list.add(2)
    empty_list.append(99)
    assert empty_list.head.value != 99
    assert empty_list.head._next._next.value == 99


def test_add_before_adds_in_the_right_place(filled_list):
    """Test that add_before places node before target value."""
    assert filled_list.head._next.value == 98
    filled_list.add_before(100, 98)
    assert filled_list.head._next.value == 100


def test_add_after_puts_node_in_the_right_position(filled_list):
    """Test that add_after puts the node after the target value node."""
    starting_node_value = filled_list.head._next.value
    filled_list.add_after(100, 76)
    assert filled_list.head._next.value != starting_node_value
    assert filled_list.head._next.value == 100
