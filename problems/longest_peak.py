from typing import List


def longestPeak(array: List[int]) -> int:
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return 1
    
    longest_peak = 0
    current_peak = 0
    previous_value = array[0]
    idx = 1
    is_increasing = False
    is_decreasing = False
    

    while idx < len(array):
        cv = array[idx]

        if cv > previous_value and not is_increasing:
            if current_peak > longest_peak and is_decreasing:
               longest_peak = current_peak
               
            current_peak = 2
            is_increasing = True
        elif cv > previous_value and is_increasing:
            current_peak += 1
        elif cv < previous_value and is_increasing:
            current_peak += 1
            is_increasing = False
            is_decreasing = True
        elif cv < previous_value and is_decreasing:
            current_peak += 1
        else:
            if current_peak > longest_peak and is_decreasing:
                longest_peak = current_peak
            
            is_increasing = False
            is_decreasing = False
            current_peak = 0

        previous_value = array[idx]
        idx += 1
    else:
        if current_peak > longest_peak and is_decreasing:
            longest_peak = current_peak
        
    return longest_peak

