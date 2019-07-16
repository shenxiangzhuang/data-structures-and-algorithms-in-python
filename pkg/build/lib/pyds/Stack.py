class Empty(Exception):
    pass


class ArrayStack:
    """
    LIFO Srtack implementation using Python list as underlyinh storage
    """
    def __init__(self):
        """Create and empty stack."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def __repr__(self):
        """
        Show the stack properly.
        """
        print("\n")
        if self.is_empty():
            s1 = '| ' + "".center(5) + ' |'
            s2 = '-' * 7
            return s1 + '\n' + s2
        else:
            s = []
            for ele in self._data:
                s1 = '| ' + ele.__repr__().center(5) + ' |'
                s2 = '-' * 7
                s.append(s1 + '\n' + s2)
            return ''.join(s)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element to the top of the stack"""
        self._data.append(e)

    def top(self):
        """
        Return (but not remove) at the top of the stack.
        Raise Empty exception if the stack in empty.
        """
        if self.is_empty():
            raise Empty("Stack in empty!")
        return self._data[-1]

    def pop(self):
        """
        Remove and return the element from the top of the stack(LIFO)
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty!")
        return self._data.pop()
