from typing import List


def isMonotonic(array: List[int]) -> bool:
    if len(array) <= 2:
        return True
    
    starting_idx = 1

    # Always will run While due to the initial length check above
    while starting_idx < len(array) - 1:
        initial_diff = array[starting_idx] = array[starting_idx - 1]
        
        if initial_diff != 0:
            break

        starting_idx += 1
    
    is_increasing = initial_diff > 0
    
    for idx in range(starting_idx, len(array) - 1):
        if is_increasing:
            if array[idx] > array[idx + 1]:
                return False
        else:
            if array[idx] < array[idx + 1]:
                return False

    return True
