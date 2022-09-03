from typing import Dict


# O(n) time | O(1) space
def getNthFib(n):
    last_two = [0, 1]
    counter = 3
    
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1

    return last_two[1] if n > 1 else last_two[0]


# O(n) time | O(n) space
def getNthFib(n, memoize: Dict = {1: 0, 2: 1}) -> int:
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        return memoize[n]


# O(n^2) time | O(n) space
def getNthFib(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)


def getNthFib(
    n: int,
    prev_1_value: int = 0,
    prev_2_value: int = 1,
    current_n: int = 2
) -> int:
    # getNthFib(1) = 0
    # getNthFib(2) = 1
    # F(n) = F(n - 1) + F(n - 2)
    if n == 1:
        return 0
    elif n == 2:
        return 1

    current_total = prev_1_value + prev_2_value

    if current_n == n:
        return current_total

    return getNthFib(
        n,
        current_total, 
        prev_1_value, 
        current_n + 1
    )

    
    
