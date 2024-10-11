from toydata.Stack import ArrayStack
from collections import deque

# R-6.1
"""
Note that:
push -> None
pop  -> top element | Empty Error
"""

# R-6.2
# 25 - 10 + 3 = 18


# R-6.3
def transfer(S: ArrayStack, T: ArrayStack) -> None:
    while not S.is_empty():
        T.push(S.pop())


def test_transfer():
    S = ArrayStack()
    S.push(3)
    S.push(2)
    S.push(1)
    print(S)
    T = ArrayStack()
    transfer(S, T)
    print(T)


# R-6.4
def stack_clear(s: ArrayStack) -> None:
    if s.is_empty():
        return
    s.pop()
    return stack_clear(s)


def test_stack_clear():
    S = ArrayStack()
    S.push(3)
    S.push(2)
    S.push(1)
    print(S)
    stack_clear(S)
    print(S)


# R-6.5
def reverse_list(items):
    s = ArrayStack()
    for item in items:
        s.push(item)
    for i in range(len(items)):
        items[i] = s.pop()


def test_reverse_list():
    items = [1, 2, 3]
    reverse_list(items)
    print(items)

# R-6.7
"""
enqueue -> None
dequeue -> first element | Empty Error
"""

# R-6.8
# 32 - 15 + 5 = 22


# R-6.9
# 15 - 5 = 10


# R-6.11
class AdapterQueue:
    def __init__(self):
        self._queue = deque()

    def __len__(self):
        return len(self._queue)

    def first(self):
        return self._queue[0]

    def is_empty(self):
        return len(self._queue) == 0

    def enqueue(self, e):
        self._queue.append(e)

    def dequeue(self):
        self._queue.popleft()


# C-6.15
"""
x = max(S.pop(), S.pop())
Note: we can assume the three numbers are: 1, 2, 3. Then,
we draw two numbers from them, there are three situations:
(1, 2), (1, 3), (2, 3). Using our algorithm, we will get
2, 3, 3, then x storing the largest of Alice’s three
integers with probability 2/3.
"""


# C-6.16
class Full(Exception):
    pass


class ArrayStackMax(ArrayStack):
    def __init__(self, maxlen=None):
        self._data = []
        self._maxlen = maxlen

    def push(self, e):
        if len(self._data) >= self._maxlen:
            raise Full("Reached the max length restriction!")
        self.push(e)


# C-6.17
class ArrayStackInitList(ArrayStack):
    def __init__(self, maxlen=None):
        self._data = [None] * maxlen
        self._maxlen = maxlen


# C-6.18
def reverse_stack(S: ArrayStack):
    s1 = ArrayStack()
    s2 = ArrayStack()
    transfer(S, s1)
    transfer(s1, s2)
    transfer(s2, S)


def test_reverse_stack():
    S = ArrayStack()
    S.push(3)
    S.push(2)
    S.push(1)
    print(S)
    reverse_stack(S)
    print(S)


# C-6.23
def three_stack(R: ArrayStack, S: ArrayStack, T: ArrayStack):
    R_len = len(R)
    while not S.is_empty():
        R.push(S.pop())
    while not T.is_empty():
        R.push(T.pop())
    while len(R) > R_len:
        S.push(R.pop())


def test_three_stack():
    R = ArrayStack()
    R.push(1)
    R.push(2)
    R.push(3)

    S = ArrayStack()
    S.push(4)
    S.push(5)

    T = ArrayStack()
    T.push(6)
    T.push(7)
    T.push(8)
    T.push(9)

    three_stack(R, S, T)
    print("R:")
    print(R)
    print("S:")
    print(S)
