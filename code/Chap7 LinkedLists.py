from typing import Any
from toydata.utils import Empty
from toydata.LinkedLists import Singlellist, Doublellist
import pysnooper

# Reinforcement


# R-7.1
def get_second_to_last(sll: Singlellist) -> Any:
    ptr = sll.head
    while ptr.next.next is not None:
        ptr = ptr.next
    return ptr.element


# R-7.2
def concatenating_linked_lists(l1: Singlellist,
                               l2: Singlellist,
                               ) -> Singlellist:
    result = Singlellist()
    result.head = l1.head
    l1.tail.next = l2.head
    return result


# R-7.3
def count_num(sll: Singlellist) -> int:
    if sll.head is None:
        return 0
    sll.remove_first()
    return 1 + count_num(sll)


# R-7.4
def sll_swap_node(sll: Singlellist, x, y) -> None:
    if x == y:
        return
    # S1: find prev_x, curr_x
    ptr = sll.head
    while ptr.next.value != x:
        ptr = ptr.next
    prev_x = ptr
    curr_x = ptr.next

    # S1: find prev_y, curr_y
    ptr = sll.head
    while ptr.next.value != y:
        ptr = ptr.next
    prev_y = ptr
    curr_y = ptr.next

    # S2: change prev
    if prev_x is None:  # x is the head
        sll.head = curr_y
    else:
        prev_x.next = curr_y

    if prev_y is None:  # y is the head
        sll.head = curr_x
    else:
        prev_y.next = curr_x

    # S3: change next
    temp = curr_x.next
    curr_x.next = curr_y.next
    curr_y.next = temp


def dll_swap_node(dll: Doublellist, x, y) -> None:
    if x == y:
        return

    # S1: find node x
    ptr = dll._header
    while ptr._element != x:
        ptr = ptr._next
    curr_x = ptr

    # S1: find node y
    ptr = dll._header
    while ptr._element != y:
        ptr = ptr._next
    curr_y = ptr

    # S2: change prev
    temp = curr_x._prev
    curr_x._prev = curr_y._prev
    curr_y._prev = temp

    # S3: change next
    temp = curr_x._next
    curr_x._next = curr_y._next
    curr_y._next = temp


# R-7.9
def concatenating_dll(l1: Doublellist,
                      l2: Doublellist) -> Doublellist:
    l1._tailer._prev._next = l2._header._next
    l2._header._next._prev = l1._tailer._prev
    return l1


# C-7.24
# Without head sentinel version :-)
class LinkedStack(Singlellist):
    """
    LIFO Srtack implementation using Python list as underlyinh storage.
    """
    def __init__(self):
        """Create and empty stack.
        """
        self._data = Singlellist()

    def __len__(self):
        """Return the number of elements in the stack.
        Time Complexity: O(1)
        """
        return len(self._data)

    def __repr__(self):
        """
        Show the stack properly.
        Time Complexity: O(1)
        """
        if self.is_empty():
            s1 = '| ' + "".center(5) + ' |' + '\n'
            s2 = '-' * 9
            return s1 + s2
        else:
            s = []
            for i in range(len(self._data) - 1, -1, -1):
                ele = self._data[i]
                s1 = '| ' + ele.__repr__().center(5) + ' |' + '\n'
                s2 = '-' * 9 + '\n'
                s.append(s1 + s2)
            return ''.join(s)

    def is_empty(self):
        """Return True if the stack is empty
        Time Complexity: O(1)
        """
        return len(self._data) == 0

    def push(self, e):
        """Add element to the top of the stack
        Time Complexity: O(1)*
        Note: "*" in here means amortization
        """
        self._data.add_first(e)

    def top(self):
        """
        Return (but not remove) at the top of the stack.
        Raise Empty exception if the stack in empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise Empty("Stack in empty!")
        return self._data.head.value

    def pop(self):
        """
        Remove and return the element from the top of the stack(LIFO)
        Raise Empty exception if the stack is empty.
        Time Complexity: O(1)*
        """
        if self.is_empty():
            raise Empty("Stack is empty!")
        ele = self._data.head.value
        self._data.remove_first()
        return ele


# C-7.28
# @pysnooper.snoop()
def reverse_sll_1(sll: Singlellist) -> Singlellist:
    if len(sll) == 1:
        return sll
    head = sll.remove_first()
    reverse_sll_1(sll).add_last(head.value)
    return sll


def reverse_sll_2(sll: Singlellist) -> Singlellist:
    if len(sll) == 1:
        return sll
    head = sll.remove_first()
    head.next = None
    reverse_sll_2(sll).tail.next = head
    sll.tail = head
    return sll


# C-7.29
def reverse_sll_loop(sll: Singlellist) -> Singlellist:
    if len(sll) == 1:
        return sll
    head = sll.head
    prev_node = None
    curr_node = sll.head
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    sll.head = sll.tail
    sll.tail = head
