from typing import List


# O(n^2) time | O(1) space
def twoNumberSum(array: List, targetSum: int) -> List:
    for idx1 in range(len(array)):
        for idx2 in range(idx1 + 1, len(array)):
            if array[idx1] + array[idx2] == targetSum:
                return [array[idx1], array[idx2]]

    return []


# O(n) time | O(n) space
def twoNumberSum(array: List, targetSum: int) -> List:
    nums = {}

    for num in array:
        potential_match = targetSum - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num] = True

    return []


# O(nlog(n)) time | O(1) space
def twoNumberSum(array: List, targetSum: int) -> List:
    array.sort()

    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]

        if current_sum == targetSum:
            return [array[left], array[right]]
        elif current_sum < targetSum:
            left += 1
        elif current_sum > targetSum:
            right -= 1

    return []
