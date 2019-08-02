import math
import numpy as np
import matplotlib.pyplot as plt
from typing import List, TypeVar
Num = TypeVar('Num', int, float)


# R-3.1
def plot_loglog():
    xs = range(1, 100)
    plt.loglog(xs, [8 * x for x in xs], basex=2, basey=2)
    plt.loglog(xs, [4 * x * np.log2(x) for x in xs], basex=2, basey=2)
    plt.loglog(xs, [2 * (x**2) for x in xs], basex=2, basey=2)
    plt.loglog(xs, [x**3 for x in xs], basex=2, basey=2)
    plt.loglog(xs, [2**x for x in xs], basex=2, basey=2)
    plt.legend(['$8n$', '$4n\\logn$', '$2n^2$', '$n^3$', '2^n'])
    plt.show()


# R-3.2
# n0 = 16

# R-3.3
# n0 = 20

# R-3.4
# Constant Function

# R-3.5
# 两边取对数，得到新的x轴，y轴

# R-3.6
# n(n+1)

# R-3.8
# Constant < linear < log * linear < exponential


# R-3.23 -> R-3.26
def get_time_complexity_1(n, func):
    op_nums = []
    for i in range(1, n):
        A = np.random.randint(0, 100, size=(i, ))
        _, num_calc = func(A)
        op_nums.append(num_calc)
    plt.plot(op_nums)
    plt.title(func.__name__)
    plt.show()


def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    count = 0
    for j in range(n):
        total += S[j]
        count += 1
    return total, count


def example2(S):
    """Return the sum of the elemnets in sequnce S."""
    n = len(S)
    total = 0
    count = 0
    for j in range(0, n, 2):
        total += S[j]
        count += 1
    return total, count


def example3(S):
    """Return the sum of the elemnets in sequnce S."""
    n = len(S)
    total = 0
    count = 0
    for j in range(n):
        for _ in range(1 + j):
            total += S[j]
            count += 1
    return total, count


def example4(S):
    """Return the sum of the elemnets in sequnce S."""
    n = len(S)
    prefix = 0
    total = 0
    count = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
        count += 1
    return total, count


# R-3.27
def example5(A, B):
    n = len(A)
    count = 0
    num_calc = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1 + j):
                total += A[k]
                num_calc += 1
        if B[i] == total:
            count += 1
    return count, num_calc


def get_time_complexity_2(n=100):
    op_nums = []
    for i in range(1, n):
        A = np.random.randint(0, 100, size=(i, ))
        B = np.random.randint(0, 100, size=(i, ))
        _, num_calc = example5(A, B)
        op_nums.append(num_calc)
    plt.plot(op_nums)
    plt.plot(range(n), [i**2 for i in range(n)])
    plt.plot(range(n), [i**3 for i in range(n)])
    plt.legend(['example5', '$n^2$', '$n^3$'])
    plt.title('example5')
    plt.show()


# R-3.32
# O(n^2)

# R-3.33
# By definition, O(nlogn) may have larger constant factor than O(n^2)

# R-3.34
# O(logn)


# C-3.35
def disjoint(a: List[Num], b: List[Num], c: List[Num]) -> bool:
    all_nums = sorted(a + b + c)
    for i in range(2, len(all_nums)):
        if all_nums[i] == all_nums[i - 1] == all_nums[i - 2]:
            return False
    return True


# C-3.36
# O(nlogn)
def max_ten_1(nums: List[Num]) -> List[Num]:
    return sorted(nums)[-10:]


# O(n)
def max_ten_2(nums: List[Num]) -> List[Num]:
    result = sorted(nums[:10])
    for i in range(10, len(nums)):
        if nums[i] > result[0]:
            result[0] = nums[i]
            result = sorted(result)
    return result


# C-3.41
def min_max(nums: List[Num]) -> List[Num]:
    min_num = math.inf
    max_num = -math.inf
    for i in range(1, len(nums), 2):
        if nums[i] >= nums[i - 1]:
            min_num = min(min_num, nums[i - 1])
            max_num = max(max_num, nums[i])
        else:
            min_num = min(min_num, nums[i])
            max_num = max(max_num, nums[i - 1])
    # when len(nums) is odd
    # we have to handle the last element
    min_num = min(min_num, nums[-1])
    max_num = max(max_num, nums[-1])
    return [min_num, max_num]


# C-3.42
# n(n-1)/2 +１


# C-3.45
def find_miss(nums: List[Num]) -> Num:
    # (n-1) -> m
    m = len(nums)
    total: float = 0
    for i in range(m):
        total += nums[i]
    return m * (m + 1) // 2 - total


# C3.53
def get_plan(n):
    person_num = len(str(bin(n))) - 2
    for i in range(n + 1):
        print(str(bin(i))[2:].rjust(person_num, '0'))


# C3.54
def get_most_freq_num(nums: List[int]) -> int:
    records = [0] * (4 * len(nums))
    for num in nums:
        records[num] += 1
    max_time = records[0]
    max_num = nums[0]
    for num, time in enumerate(records):
        if time > max_time:
            max_time = time
            max_num = num
    return max_num
