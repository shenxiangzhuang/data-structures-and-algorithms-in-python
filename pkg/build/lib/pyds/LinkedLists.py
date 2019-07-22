from pyds.utils import Empty


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


class Singlellist:
    """
    The implementation of single linked list.

    Support operations:
    [built-in]
    len, print, in
    [add]
    add_first, add_last, insert_after, insert_before
    [remove]
    remove_first, remove_last, remove_after, remove_before
    [update]
    change_first, change_all
    [search]
    search
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

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
        self.head = self.head.next
        self.size -= 1

    def remove_last(self):
        """
        Remove the last element in the single linked list.
        Or raise an empty error when there is no node in the list.
        """
        if self.is_empty():
            raise Empty("The single linked list is empty")
        pointer = self.head
        while pointer.next != self.tail:
            pointer = pointer.next
        self.tail = pointer
        self.next = None
