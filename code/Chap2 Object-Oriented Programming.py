import numbers
import time
from math import sqrt
from abc import ABCMeta, abstractmethod
from typing import TypeVar, Union, Any
from random import randint
import matplotlib.pyplot as plt
Num = TypeVar('Num', int, float)


# R-2.4
class Flower:
    def __init__(self, name: str, n_petals: int, price: Num) -> None:
        self._name = name
        self._n_petals = n_petals
        self._price = price

    def get_name(self) -> str:
        '''get flower name'''
        return self._name

    def set_name(self, name: str) -> None:
        '''set flower name'''
        self._name = name

    def get_n_petals(self) -> int:
        '''get the num of flower'petrals'''
        return self._n_petals

    def set_n_petals(self, n_petals: int) -> None:
        '''set the num of flower'petrals'''
        self._n_petals = n_petals

    def get_price(self) -> Num:
        '''get flower price'''
        return self._price

    def set_price(self, price) -> None:
        '''set flower price'''
        self._price = price


# R-2.5, 2.6, 2.7
class CrediCart:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._cunstomer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance

    def charge(self, price: Num):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        try:
            assert isinstance(price, (int, float, complex))
        except AssertionError:
            print("The price must be a number!")
            # exit the function
            return
        # if charge would exceed limit,
        if price + self._balance > self._limit:
            return False
        # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        # is a number or not
        try:
            assert isinstance(amount, numbers.Number)
        except AssertionError:
            print("The amount must be a number!")
            # exit the function
            return
        # is positive or not
        if amount < 0:
            raise ValueError("amount must be a positive number")
        """Process customer payment that reduces balance."""
        self._balance -= amount


# R-2.9 -> R-2.15
class Vector:
    def __init__(self, data_or_n: Any) -> None:
        if isinstance(data_or_n, int):
            self._data = [0] * data_or_n
            self._len = data_or_n
        elif isinstance(data_or_n, list):
            self._data = data_or_n
            self._len = len(data_or_n)
        else:
            raise ValueError("Vector must be initialized by a int or list!")

    def __repr__(self) -> str:
        return repr(self._data).replace('[', '<').replace(']', '>')

    def __len__(self):
        return self._len

    def __getitem__(self, index: int) -> Num:
        return self._data[index]

    def __setitem__(self, index: int, value: Num) -> None:
        self._data[index] = value

    def __add__(self, v: 'Vector') -> 'Vector':
        """
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([1, 1, 1])
        >>> v1 + v2
        <2, 3, 4>
        """
        assert len(self) == len(v)
        result = Vector(self._len)
        for i in range(len(self)):
            result[i] = self._data[i] + v[i]
        return result

    def __radd__(self, v: 'Vector') -> 'Vector':
        return self.__add__(v)

    def __sub__(self, v: 'Vector') -> 'Vector':
        """
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([1, 1, 1])
        >>> v1 - v2
        <0, 1, 2>
        """
        assert len(self) == len(v)
        result = Vector(self._len)
        for i in range(len(self)):
            result[i] = self._data[i] - v[i]
        return result

    def __neg__(self) -> 'Vector':
        """
        >>> -Vector([1, 2, 3])
        <-1, -2, -3>
        """
        result = Vector(self._len)
        for index, value in enumerate(self._data):
            result[index] = -value
        return result

    def __mul__(self, factor: Union[int, 'Vector']) -> Union[int, 'Vector']:
        """multiply with an int or vector.
        >>> v1 = Vector([1, 2, 3])
        >>> v1 * 2
        <2, 4, 6>
        >>> 2 * v1
        <2, 4, 6>
        >>> v2 = Vector([1, 1, 1])
        >>> v1 * v2
        6
        """
        if isinstance(factor, Vector):
            assert len(self) == len(factor)
            result = 0
            for i in range(self._len):
                result += self._data[i] * factor[i]
            return result
        else:
            result = Vector(self._len)
            for index, value in enumerate(self._data):
                result[index] = factor * value
            return result

    def __rmul__(self, factor: Union[int, 'Vector']) -> Union[int, 'Vector']:
        return self.__mul__(factor)


# R-2.18
class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for i in range(n)))


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        # initialize base class
        # start progression at first
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._current + self._prev


# The solution
# fib = FibonacciProgression(2, 2)
# fib.print_progression(8)

# R-2.19
steps = 2**(63 - 7)


# C-2.26
class ReversedSequenceIterator:
    """
    A reversed iterator for Python's sequence types.
    """
    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self._seq = sequence
        self._k = len(sequence)

    def __next__(self):
        """Return the next element(with reversed order), or else
        raise StopIteration error"""
        self._k -= 1
        if self._k >= 0:
            return self._seq[self._k]
        else:
            raise StopIteration

    def __iter__(self):
        return self


# R-2.27
class Range:
    """A class that mimic's the build-in range class"""
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot ne 0')
        # special case for range(n)
        if stop is None:
            start, stop = 0, start
        # calculate the effective length once
        self._length = max(0, (step - start + step - 1) // step)
        # need knowledge of the start and step(but not stop)
        # to support __getitem__
        self._start = start
        self._step = step
        # for __contains
        self._stop = stop

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        # negative index
        if k < 0:
            k += self._length

        if not 0 <= k < self._length:
            raise IndexError("index out of range")

        return self._start + k * self._step

    def __contains__(self, x):
        if not self._start <= x < self._stop:
            return False
        if (x - self._start) % self._step == 0:
            return True
        else:
            return False

    @staticmethod
    def test_contains(start=0, stop=10000000, step=1, test_n=50):
        xs = sorted([randint(start, stop) for i in range(test_n)])
        times = []
        my_range = Range(start, stop, step)
        for x in xs:
            time_s = time.time()
            x in my_range
            times.append(time.time() - time_s)
        plt.plot(xs, times)
        plt.ylim(0, 0.00002)
        plt.show()


# C-2.31
class AbsdiffPrograssion(Progression):
    def __init__(self, first=2, second=200):
        super().__init__(first)
        self._prev1 = None
        self._prev2 = None
        # for starting
        self._second = second
        self._count = 1

    def _advance(self):
        # for starting
        if self._count == 1:
            self._prev1 = self._current
            self._current = self._second
        else:
            self._prev1, self._prev2 = self._current, self._prev1
            self._current = abs(self._prev1 - self._prev2)
        self._count += 1


# C-2.32
class SquareRootProgression(Progression):
    def __init__(self, start=65536):
        super().__init__(start)

    def _advance(self):
        self._current = sqrt(self._current)
