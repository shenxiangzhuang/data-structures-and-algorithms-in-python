from typing import List, TypeVar, Tuple, Any
from functools import lru_cache
Num = TypeVar('Num', int, float)


# R-4.1
# time: O(n); space: O(1)
def max_recursion(nums: List[Num], n: int) -> Num:
    if n == 1:
        return nums[0]
    return max(nums[n - 1], n - 1)


# R-4.6
def harmonic_recursion_1(n: int) -> Num:
    if n == 1:
        return n
    return 1 / n + harmonic_recursion_1(n - 1)


# python doesn't support tail-call optimization
def harmonic_recursion_2(n: int, acc=0) -> Num:
    if n == 0:
        return acc
    return harmonic_recursion_2(n - 1, acc + 1 / n)


@lru_cache(maxsize=None)
def harmonic_recursion_3(n: int) -> Num:
    if n == 1:
        return n
    return 1 / n + harmonic_recursion_1(n - 1)


# R-4.7
def char_to_int(char: str) -> int:
    """
    convert the single number with str type to number type
    """
    return ord(char) - ord('0')


def str_to_int(string: str, n: int) -> int:
    if n == 1:
        return char_to_int(string[0])
    return char_to_int(string[n - 1]) * (10 ** (n - 1)) \
        + str_to_int(string, n - 1)


# R-4.8
# O(n)


# C-4.9
def my_min(n1: Num, n2: Num) -> Num:
    if n1 >= n2:
        return n2
    else:
        return n1


def my_max(n1: Num, n2: Num) -> Num:
    if n1 >= n2:
        return n1
    else:
        return n2


def min_max_num(nums: List[Num], n: int) -> Tuple[Num, Num]:
    if n == 1:
        return (nums[0], nums[0])
    return (
        my_min(nums[n - 1],
               min_max_num(nums, n - 1)[0]),
        my_max(nums[n - 1],
               min_max_num(nums, n - 1)[1]),
    )


# C-4.10
def get_log_int(n: Num) -> int:
    assert n > 0
    if n < 2:
        return 0
    return 1 + get_log_int(n // 2)


# C-4.11
def one_diff_all(element: Any, seq: List[Any], length: int) -> bool:
    for i in range(length):
        if element == seq[i]:
            return False
    return True


def is_unique(seq: List[Any], n: int) -> bool:
    if n == 1:
        return True
    return is_unique(seq, n - 1) and one_diff_all(seq[n - 1], seq, n - 1)


'''
Haskell:
allDifferent :: (Eq a) => [a] -> Bool
allDifferent list = case list of
    []      -> True
    (x:xs)  -> x `notElem` xs && allDifferent xs
'''


# C-4.12
def multiply(m: int, n: int) -> int:
    if n == 1:
        return m
    return m + multiply(m, n - 1)


# C-4.15
def get_subsets(s: List[Any], n: int) -> List[Any]:
    if n == 0:
        return [[]]
    return [[s[n - 1]] + i
            for i in get_subsets(s, n - 1)] + get_subsets(s, n - 1)


# C-4.16
def reverse_str(s: str, n: int) -> str:
    if n == 1:
        return s[0]
    return s[n - 1] + reverse_str(s, n - 1)


# C-4.17
# 递归中一种常见隐藏细节的方法，可以使得调用更加简单
def is_palindrome(s: str) -> bool:
    def judge(s: str, start: int, end: int) -> bool:
        n = end - start + 1
        if n <= 1:
            return True
        return (s[start] == s[end]) and judge(s, start + 1, end - 1)

    return judge(s, 0, len(s) - 1)


# C-4.18
def count_vowels(s: str, n: int) -> int:
    vowels = 'aeiouAEIOU'
    if n == 0:
        return 0
    if s[n - 1] in vowels:
        return 1 + count_vowels(s, n - 1)
    else:
        return count_vowels(s, n - 1)


def is_more_vowel(s: str) -> bool:
    num_vowel = count_vowels(s, len(s))
    num_consonants = len(s) - num_vowel
    if num_vowel > num_consonants:
        return True
    else:
        return False


# c-4.19
def even_before_odd(nums: List[int]) -> List[int]:
    if not nums:
        return []
    if nums[0] % 2 == 0:
        return [nums[0]] + even_before_odd(nums[1:])
    else:
        return even_before_odd(nums[1:]) + [nums[0]]


# C-4.20
def seperate_by_k(nums: List[int], k: int) -> List[int]:
    if not nums:
        return []
    if nums[0] <= k:
        return [nums[0]] + seperate_by_k(nums[1:], k)
    else:
        return seperate_by_k(nums[1:], k) + [nums[0]]


# C-4.21
def sum_to_k(nums: List[int], k: int, start: int, end: int) -> List[int]:
    assert len(nums) > 2
    if start == end:
        return []
    if nums[start] + nums[end] == k:
        return [nums[start], nums[end]]
    elif nums[start] + nums[end] < k:
        return sum_to_k(nums, k, start + 1, end)
    else:
        return sum_to_k(nums, k, start, end - 1)


# C-4.22
def power(x: int, n: int):
    result = 1
    while n > 0:
        while n & 1 == 0:
            n //= 2
            result *= result
        result *= x
        n -= 1
    return result
