from typing import List


def productSum(
    array: List,
    depth: int = 1
) -> int:
    total = 0

    for i in array:
        if isinstance(i, int):
            total += i
        elif isinstance(i, list):
            total += productSum(i, depth + 1)

    return depth * total
