import re
from typing import List, TypeVar, Tuple, Any, Generator
from random import randrange, randint
Num = TypeVar('Num', int, float)


# R-1.1
def is_multiple(n: int, m: int) -> bool:
    return True if n % m == 0 else False


# R-1.2
def is_even(k: int) -> bool:
    return False if k & 1 else True


# R-1.3
def minmax(data: List[Num]) -> Tuple[Num, Num]:
    min_num = max_num = data[0]
    for num in data:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num


# R-1.4, R-1.5
def sum_sq(n: int) -> int:
    return sum(i * i for i in range(1, n))


# R-1.6, R-1.7
def sum_odd_sq(n: int) -> int:
    return sum(i * i for i in range(1, n) if not is_even(i))


# R-1.8(j = n + k <=> k = j - n)
def check(data: str = 'hello') -> bool:
    n = len(data)
    for j in range(n):
        k = j - n
        if data[j] != data[k]:
            return False
    return True


# R-1.9
print(list(range(50, 90, 10)))

# R-1.10
print(list(range(8, -10, -2)))

# R-1.11
print([2**i for i in range(9)])


# R-1.12
def choice(data: List[Any]) -> Any:
    return data[randrange(0, len(data))]


# C-1.13
def reverse(data: List[Any]) -> List[Any]:
    n = len(data)
    return [data[i] for i in range(n - 1, -1, -1)]


# C-1.14
def odd_pair(data: List[int]) -> bool:
    odd_nums = {num for num in data if not is_even(num)}
    return True if len(odd_nums) >= 2 else False


# C-1.15
def is_unique(data: List[Num]) -> bool:
    return len(data) == len(set(data))


# C-1.16
# Think about the semantics of data[j] = data[j] ∗ factor.


# C-1.17(This doesn't work. It just create a new local var: val)
def scale(data, factor):
    for val in data:
        val *= factor


# C-1.18
print([i * (i + 1) for i in range(0, 10)])

# C-1.19
print([chr(ord('a') + i) for i in range(0, 26)])


# C-1.20
def shuffle(data: List[Any]) -> None:
    n = len(data)
    for i in range(n - 1, 0, 1):
        j = randint(0, i - 1)
        data[i], data[j] = data[j], data[i]


# C-1.21
def print_reverse() -> None:
    lines = []
    while 1:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)
    for line in reversed(lines):
        print(line)


# C-1.22
def array_product(a: List[int], b: List[int]) -> List[int]:
    return [i * j for i, j in zip(a, b)]


# C-1.23
def check_overflow() -> None:
    data = [1, 2, 3]
    try:
        data[randint(0, 3)] = 0
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")


# C-1.24
def get_vowels(data: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([i for i in data.lower() if i in vowels])


# C-1.25
def remove_punctuation(sentence: str) -> str:
    removed = [
        char for char in sentence
        if (ord('A') <= ord(char) <= ord('z')) or ord(char) == ord(' ')
    ]
    print(removed)
    return ''.join(removed)


# C-1.26
def check_op_right() -> bool:
    nums = input("input int a, b, c: ")
    operators = '+-*/'

    # case1: a = b op c
    a, b_c_str = re.findall(r'(\d+), (\d+, \d+)', nums)[0]
    case1 = [int(a) == eval(b_c_str.replace(', ', op)) for op in operators]
    result = sum(case1)

    # case2: a op b = c
    a_b_str, c = re.findall(r'(\d+, \d+), (\d+)', nums)[0]
    case2 = [int(c) == eval(a_b_str.replace(', ', op)) for op in operators]
    result += sum(case2)

    return result > 0


# C-1.27
def factors(n: int) -> Generator[int, None, None]:
    k = 1
    larger_factors = []
    while k * k < n:
        if n % k == 0:
            yield k
            larger_factors.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for num in reversed(larger_factors):
        yield num


# C-1.28
def norm(v: List[Num], p: int = 2) -> Num:
    return sum(i**p for i in v)**(1 / p)


# P-1.29
def add_char(char: str, string_list: List[str]) -> List[str]:
    return [char + string for string in string_list]


def flatten_lists(lists: List[List[Any]]) -> List[Any]:
    result = []
    for l1 in lists:
        result += l1
    return result


def permutation(chars: str) -> List[str]:
    # Base case
    if len(chars) == 1:
        return [chars]
    return flatten_lists([
        add_char(chars[i], permutation(chars[:i] + chars[i + 1:]))
        for i in range(len(chars))
    ])


# P-1.30
def my_log(n: int) -> int:
    if n < 2:
        return 0
    elif n < 4:
        return 1
    return 1 + my_log(n / 2)
