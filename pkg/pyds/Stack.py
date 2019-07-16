from pyds.utils import Empty


class ArrayStack:
    """
    LIFO Srtack implementation using Python list as underlyinh storage.
    """
    def __init__(self):
        """Create and empty stack.
        Space Complexity: O(n)
        """
        self._data = []

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
            for i in range(len(self._data)-1, -1, -1):
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
        self._data.append(e)

    def top(self):
        """
        Return (but not remove) at the top of the stack.
        Raise Empty exception if the stack in empty.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise Empty("Stack in empty!")
        return self._data[-1]

    def pop(self):
        """
        Remove and return the element from the top of the stack(LIFO)
        Raise Empty exception if the stack is empty.
        Time Complexity: O(1)*
        """
        if self.is_empty():
            raise Empty("Stack is empty!")
        return self._data.pop()
