from typing import List


def swap(lst: List, pos_1: int, pos_2: int):
    lst[pos_1], lst[pos_2] = lst[pos_2], lst[pos_1]


def moveElementToEnd(array: List[int], to_move: int) -> List[int]:
    l_idx = 0
    r_idx = len(array) - 1

    while l_idx < r_idx:
        if array[r_idx] == to_move:
            r_idx -= 1
            continue
        elif array[l_idx] == to_move:
            swap(array, l_idx, r_idx)
            r_idx -= 1
        elif array[r_idx] == to_move:
            r_idx -= 1
        l_idx += 1

    return array
