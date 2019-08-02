import sys
import pandas as pd
import random
from time import time
import ctypes
from typing import List, TypeVar
Num = TypeVar('Num', int, float)


# R-5.1
def test_array_1(n=27):
    data = []
    for _ in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(None)


# R-5.2
def test_array_2(n=27):
    data = []
    max_size = 0
    for _ in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        # 第一次打印
        if max_size == 0:
            max_size = b
        if b > max_size:
            print('Length: {0:3d}; Size in bytes: {1:4d}'
                  .format(a - 1, max_size))
            max_size = b
        data.append(None)


# R-5.3
def test_array_3(n=27):
    data = [None] * n
    for _ in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.pop()


# R-5.4
class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""
    def __init__(self):
        """Create an empty array"""
        self._n = 0                                    # count actual elements
        self._capacity = 1                             # default array capacity
        self._A = self._make_array(self._capacity)     # low-level array

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n

    def __getitem__(self, k):
        """Return element at index k"""
        # 添加对负数索引的支持
        if k < 0:
            k += self._n
        # 索引查验
        if not 0 <= k <= self._n:
            raise IndexError('invalid index')
        return self._A[k]

    # 为了便于查看
    def __repr__(self):
        if self._n == 0:
            return 'Array[]'
        return 'Array[' + ', '.join(str(self._A[i])
                                    for i in range(self._n)) + ']'

    def append(self, obj):
        """Add object to end of array"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()


# R-5.6
class DynamicArrayInsert(DynamicArray):
    """A dynamic array class akin to a simplified Python list"""

    def __init__(self):
        """Create an empty array"""
        super().__init__()

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent value rightward"""
        if self._n == self._capacity:
            B = self._make_array(self._capacity * 2)
            for i in range(k):
                B[i] = self._A[k]
            B[k] = value
            for j in range(k + 1, self._n + 1):
                B[j] = self._A[j - 1]
            self._A = B
            self._n += 1
            self._capacity *= 2
        else:
            for i in range(self._n, k, -1):
                self._A[i] = self._A[i - 1]
            self._A[k] = value
            self._n += 1


# R-5.7
def find_dup(nums):
    n = len(nums)
    return sum(nums) - n * (n - 1) // 2


# R-5.8
def benchmark(test_func):
    insert_df = pd.DataFrame(index=['start', 'middle', 'end'],
                             columns=['100', '1000', '10000', '100000'])
    insert_df.index.name = 'Time(microseconds)'
    for n in list(insert_df.columns):
        insert_df[n] = [test_func(int(n), mode) for mode in insert_df.index]
    return insert_df


# insert测试
def insert_average(n, mode='start'):
    data = []
    start = time()
    if mode == 'start':
        for _ in range(n):
            data.insert(0, None)
    elif mode == 'middle':
        for _ in range(n):
            data.insert(n // 2, None)
    elif mode == 'end':
        for _ in range(n):
            data.insert(n, None)
    end = time()
    return (end - start) * 1000000 / n

benchmark(insert_average)


# pop测试
def pop_average(n, mode='start'):
    data = [None] * n
    start = time()
    if mode == 'start':
        for _ in range(n):
            data.pop(0)
    elif mode == 'middle':
        count = n
        while count > 0:
            data.pop(count // 2)
            count -= 1
    elif mode == 'end':
        for _ in range(n):
            data.pop(-1)
    end = time()
    return (end - start) * 1000000 / n

benchmark(pop_average)


# R-5.10
class CaeserCipher:
    def __init__(self, shift):
        self._forward = ''.join(chr((k + shift) % 26 + ord('A'))
                                for k in range(26))
        self._backward = ''.join(chr((k - shift) % 26 + ord('A'))
                                 for k in range(26))


# R-5.11
def sum_matrix(matrix: List[List[Num]]) -> Num:
    result: float = 0
    for raw in matrix:
        for num in raw:
            result += num
    return result


# R-5.12
def sum_matrix_plus(matrix: List[List[Num]]) -> Num:
    return sum(num for raw in matrix for num in raw)


# C-5.14
def shuffule(nums: List[Num]) -> List[Num]:
    return sorted(nums, key=lambda x: random.random())


# C-5.16
class DynamicArrayInsertPop(DynamicArrayInsert):
    """
    Implement a pop method for the DynamicArray class.
    """
    def __init__(self):
        """Create an empty array"""
        super().__init__()

    def pop(self):
        element = self._A.pop()
        if self._n < self._capacity // 4:
            self._resize(self._capacity // 2)
        return element


# C-5.21
document = 'Hello, World!' * 1000


def w1_concatenation():
    """
    1.95 ms ± 146 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    """
    letters = ''
    for c in document:
        if c.isalpha():
            letters += c
    return letters


def w2_appending():
    """
    1.71 ms ± 155 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    """
    temp = []
    for c in document:
        if c.isalpha():
            temp.append(c)
    letters = ''.join(temp)
    return letters


def w3_list_comp():
    """
    1.26 ms ± 223 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    """
    letters = ''.join([c for c in document if c.isalpha()])
    return letters


def w4_generator():
    """
    1.66 ms ± 318 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    """
    letters = ''.join(c for c in document if c.isalpha())
    return letters


# C-5.31
def binary_sum(S: List[List[float]], start: int, stop: int) -> float:
    if start >= stop:
        return 0
    if start == stop - 1:
        return sum(S[start])
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


binary_sum([[1.0, 2], [3, 4]], 0, 2)
