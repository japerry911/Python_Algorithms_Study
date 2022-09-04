from typing import List


# O(nlogn) time | O(1) space
def nonConstructibleChange(coins: List[int]):
    min_change = 0
    coins.sort()

    for c in coins:
        if c > min_change + 1:
            return min_change + 1
        else:
            min_change += c

    return min_change + 1
