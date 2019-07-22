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
