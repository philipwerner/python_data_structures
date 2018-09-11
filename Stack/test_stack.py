"""Test module for Stack class."""
from stack import Stack
import pytest


# *****Fixtures*****
@pytest.fixture
def empty_stack():
    """Create an empty stack object."""
    return Stack()


@pytest.fixture
def filled_stack():
    """Create a filled stack object."""
    x = Stack([12, 31, 41, 32, 65, 76, 3, 9])
    return x


# *****Tests*****
def test_stack_can_be_created():
    """Test that a stack can be instantiated."""
    s = Stack()
    assert isinstance(s, Stack)


def test_stack_can_be_created_with_iter():
    """Test a Stack can be created with an iterable."""
    s = Stack([1, 2, 3, 4, 5, 6])
    assert isinstance(s, Stack)


def test_add_works(empty_stack):
    """Test that empty_stack top value will be 99."""
    empty_stack.add(99)
    assert empty_stack.top.value == 99


def test_add_works_with_multiple_adds(empty_stack):
    """Test that adding 20 nodes, the top value will be 19."""
    for x in range(20):
        empty_stack.add(x)
    assert empty_stack.top.value == 19


def test_height_method_works_on_empty_stack(empty_stack):
    """Test that height method returns 0 on empty Stack."""
    assert empty_stack.height == 0


def test_height_works_while_adding_20_nodes(empty_stack):
    """Test that proper height is returned while adding 20 nodes."""
    for x in range(20):
        empty_stack.add(x)
        assert empty_stack.height == x + 1


def test_height_method_works_on_filled_stack(filled_stack):
    """Test height method returns 8 on filled_stack."""
    assert filled_stack.height == 8


def test_height_goes_up_when_add_to_stack(empty_stack):
    """Test that height returns 1 after adding to empty stack."""
    empty_stack.add(9)
    assert empty_stack.height == 1


def test_pop_method_returns_proper_value(filled_stack):
    """Test that pop returns 9 from filled stack."""
    assert filled_stack.pop() == 9
