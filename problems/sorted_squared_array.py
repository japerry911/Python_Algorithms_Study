from typing import List


# O(nlogn) time | O(n) space
def sortedSquaredArray(array: List) -> List:
    for idx in range(len(array)):
        array[idx] = array[idx] ** 2

    array.sort()

    return array


# O(n) time | O(n) space
def sortedSquaredArray(array: List):
    sorted_squares = [0 for _ in array]
    smaller_value_idx = 0
    larger_value_idx = len(array) - 1

    for idx in reversed(range(len(array))): 
        smaller_value = array[smaller_value_idx]
        larger_value = array[larger_value_idx]

        if abs(smaller_value) > abs(larger_value):
            sorted_squares[idx] = smaller_value ** 2
            smaller_value_idx += 1
        else:
            sorted_squares[idx] = larger_value ** 2
            larger_value_idx -= 1

    return sorted_squares
