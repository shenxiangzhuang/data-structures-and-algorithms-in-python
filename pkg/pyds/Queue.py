from pyds.utils import Empty


class ArrayQueue:
    """
    FIFO queue implementation using Python list
    as unedrlying storage.
    """
    # moderate capacity for all new queues
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._font = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def __repr__(self):
        if self.is_empty():
            return "Empty Queue"
        s = []
        for index, ele in enumerate(self._data):
            back = (self._font + self._size - 1) % len(self._data)
            if ele is None:
                ele_str = f"| None |"
            # back and font
            elif index == self._font == back:
                ele_str = "| " + f"->{str(ele)}<-".center(5) + " |"
            # font
            elif index == self._font:
                ele_str = "| " + f"->{str(ele)}".center(5) + " |"
            # back
            elif index == back:
                ele_str = "| " + f"{str(ele)}<-".center(5) + " |"
            else:
                ele_str = "| " + f"{str(ele)}".center(5) + " |"
            s.append(ele_str)
        return ''.join(s)

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """
        Return the first element.
        Raise Empty Error if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty!")
        return self._data[self._font]

    def dequeue(self):
        """
        Remove and return the first element.
        Raise Empty error if queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty!")
        answer = self._data[self._font]
        # help garbage collection
        self._data[self._font] = None
        self._font = (self._font + 1) % len(self._data)
        self._size -= 1
        # shrinks
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        """
        Add an element to the back of the queue
        """
        if len(self._data) == self._size:
            self._resize(len(self._data) * 2)
        avail = (self._font + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """
        Resize to a new list of capacity >= len(self)
        Note: we assume cap > len(self)
        """
        old = self._data
        self._data = [None] * cap
        walk = self._font
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._font = 0


class ArrayDeque(ArrayQueue):
    # moderate capacity for all new queues
    def __init__(self):
        super().__init__()

    def last(self):
        back = (self._font + self._size - 1) % len(self._data)
        return self._data[back]

    def add_last(self, e):
        self.enqueue(e)

    def delete_last(self):
        if self.is_empty():
            raise Empty('Dequeue is empty!')
        answer = self.last()
        back = (self._font + self._size - 1) % len(self._data)
        self._data[back] = None
        self._size -= 1
        # shrinks
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def first(self):
        return self._data[self._font]

    def add_first(self, e):
        if len(self._data) == self._size:
            self._resize(self._size * 2)
        self._font = (self._font - 1) % len(self._data)
        self._data[self._font] = e
        self._size += 1

    def delete_first(self):
        self.dequeue()
