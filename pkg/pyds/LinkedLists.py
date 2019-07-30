from pyds.utils import Empty
from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional['Node'] = None

    def __repr__(self):
        return f"Node({self.value})"


class Singlellist:
    """
    The implementation of single linked list.

    Support operations:
    [built-in]
    len, print, in, []
    [add]
    add_first, add_last, insert_after
    [remove]
    remove_first, remove_last, remove, remove_all
    [update]
    change_first, change_all
    [search]
    search
    """

    def __init__(self, items=None):
        self.head = None
        self.tail = None
        self.size = 0
        if items:
            for item in items:
                self.add_last(item)

    def __len__(self):
        return self.size

    def __repr__(self):
        items = []
        pointer = self.head
        while pointer is not None:
            items.append(pointer.value)
            pointer = pointer.next
        return f"SLL{items}"

    def __contains__(self, value):
        """
        Check if there is a value in the list, support for `in`
        """
        points = self.head
        while points is not None:
            if points.value == value:
                return True
            points = points.next
        return False

    def __getitem__(self, index):
        assert 0 <= index <= (len(self) - 1), "Index out of range"
        p = self.head
        while index > 0:
            p = p.next
            index -= 1
        return p.value

    def __setitem__(self, index, val):
        assert 0 <= index <= (len(self) - 1), "Index out of range"
        p = self.head
        while index > 0:
            p = p.next
            index -= 1
        p.value = val

    def is_empty(self):
        return self.size == 0

    def add_first(self, value):
        """
        Inserting an element at the head of a single linked list
        """
        new_node = Node(value)
        # empty list
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_last(self, value):
        """
        Adding element at the end of single linked list
        """
        new_node = Node(value)
        # empty list
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_after(self, pos_value, insert_value):
        """
        Insert the insert_value after the (first)pos_value
        """
        assert pos_value in self, f"There is no {pos_value} in list"
        insert_node = Node(insert_value)
        pointer = self.head
        while pointer.value != pos_value:
            pointer = pointer.next
        insert_node.next = pointer.next
        pointer.next = insert_node
        self.size += 1

    def remove_first(self):
        """
        Remove the first element at the single linked list.
        Or raise an empty error when there is no node in the list.
        """
        if self.is_empty():
            raise Empty("The single linked list is empty")
        answer = self.head
        self.head = self.head.next
        self.size -= 1
        return answer

    def remove_last(self):
        """
        Remove the last element in the single linked list.
        Or raise an empty error when there is no node in the list.
        """
        if self.is_empty():
            raise Empty("The single linked list is empty")
        answer = self.tail
        # when head = tail, we should change head too.
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            pointer = self.head
            while pointer.next != self.tail:
                pointer = pointer.next
            self.tail = pointer
            self.tail.next = None
        self.size -= 1
        return answer

    def remove(self, val):
        """
        Remove the first node with value equals to val.
        """
        assert val in self, f"{val} don't in list!"
        p = self.head
        # val in the head of the list
        if p.value == val:
            self.remove_first()
        else:
            while p.next.value != val:
                p = p.next
            # val in the end of the list
            if p.next.next is None:
                self.tail = p
            p.next = p.next.next
            self.size -= 1

    def remove_all(self, val):
        """
        Remove all the node woth value = val
        """
        while val in self:
            self.remove(val)

    def change(self, old_val, new_val):
        """
        Change the first node with value "old_val" to "new_val"
        """
        assert old_val in self, f"{old_val} not in list!"
        p = self.head
        while p.value != old_val:
            p = p.next
        p.value = new_val

    def change_all(self, old_val, new_val):
        """
        Change all the node with "old_val" to "new_val"
        """
        while old_val in self:
            self.change(old_val, new_val)

    def search(self, value):
        return value in self


# Here we used the class only for the
# implementation of LinkedDeque
class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation"""

    class _Node:
        """Lightweight, nonpublic class for storing a double linked node"""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._tailer = self._Node(None, None, None)
        self._header._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0

    def __Len__(self):
        """Return the number of elements in the list"""
        return self._size

    def is_empty(self):
        """Return true if the list is empty"""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node.
        With a leading underscore because we do not intend for it to provide
        a coherent public interface for gneral use.
        """
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list"""

    def first(self):
        """Return(but not remove) the element at the front of the queue"""
        if self.is_empty():
            raise Empty("Deque is empty!")
        return self._header._next._element

    def last(self):
        """Return(but not remove) the element at the back of the deque"""
        if self.is_empty():
            raise Empty("Deque is empty!")
        return self._tailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Add an element to the back if the deque"""
        self._insert_between(e, self._tailer._prev, self._tailer)

    def delete_first(self):
        """Remove and return the element from the front of the deque
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty!")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty!")
        return self._delete_node(self._tailer._prev)


class Doublellist:
    """Double linked list(with sentinels)

    Support operations:
    [built-in]
    len, print, in
    [add]
    add_first, add_last, insert_after
    [remove]
    remove_first, remove_last, remove, remove_all
    [update]
    change_first, change_all
    [search]
    search
    """

    class _Node:
        """Lightweight, nonpublic class for storing a
        doubly linked node."""
        # streamline memory
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            """Create a Node"""
            self._element = element
            self._prev = prev
            self._next = next
        
        def __repr__(self):
            return f"[~|{self._element}|~]"

    def __init__(self):
        """Create a empty list"""
        self._header = self._Node(None, None, None)
        self._tailer = self._Node(None, None, None)
        self._size = 0
        # note that we must link the header and tailer firstly
        self._header._next = self._tailer
        self._tailer._prev = self._header

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __repr__(self):
        result = ''
        result += 'Header'
        i = self._size
        ptr = self._header
        while i > 0:
            result += '->' + str(ptr._next)
            ptr = ptr._next
            i -= 1
        result += '->Tailer'
        return result

    def __contains__(self, val):
        ptr = self._header
        i = self._size
        while i > 0:
            if ptr._next._element == val:
                return True
            ptr = ptr._next
            i -= 1
        return False

    def first(self):
        if self._size == 0:
            raise Empty('The list is empty!')
        return self._header._next._element

    def last(self):
        if self._size == 0:
            raise Empty('The list is empty!')
        return self._tailer._prev._element

    def add_first(self, e):
        new_node = self._Node(e, self._header, self._header._next)
        self._header._next._prev = new_node
        self._header._next = new_node
        self._size += 1

    def add_last(self, e):
        new_node = self._Node(e, self._tailer._prev, self._tailer)
        self._tailer._prev._next = new_node
        self._tailer._prev = new_node
        self._size += 1

    def insert_after(self, pos_val, ins_val):
        # make sure there are a pos_val in list
        assert pos_val in self, f"{pos_val} not in list!"
        ptr = self._header
        while ptr._element != pos_val:
            ptr = ptr._next
        new_node = self._Node(ins_val, ptr, ptr._next)
        ptr._next._prev = new_node
        ptr._next = new_node
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty("The list is empty!")
        element = self.first()
        self._header._next._next._prev = self._header
        self._header._next = self._header._next._next
        self._size -= 1
        return element

    def remove_last(self):
        if self.is_empty():
            raise Empty("The list is empty!")
        element = self.first()
        self._tailer._prev._prev = self._tailer
        self._tailer._prev = self._tailer._prev._prev
        self._size -= 1
        return element

    def remove(self, val):
        """
        Only remove the first node with val equals `val`
        """
        assert val in self, f"{val} not in list!"
        ptr = self._header
        while ptr._next._element != val:
            ptr = ptr._next
        ptr._next._next._prev = ptr
        ptr._next = ptr._next._next
        self._size -= 1

    def remove_all(self, val):
        """
        Remove all the nodes with val equals `val`
        Note: here we use an efficient way to do that
        """
        while val in self:
            self.remove(val)

    def change(self, old_val, new_val):
        """
        Only change the first node with `old_val` to `new_val`
        """
        ptr = self._header
        while ptr._next._element != old_val:
            ptr = ptr._next
        ptr._next._element = new_val

    def change_all(self, old_val, new_val):
        """
        Change all the node with `old_val` to `new_val`
        Note: here we use an efficient way to do that        
        """
        while old_val in self:
            self.change(old_val, new_val)

    def search(self, val):
        return val in self
