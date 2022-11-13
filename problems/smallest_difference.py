from typing import List


def smallestDifference(array_one: List[int], array_two: List[int]) -> List[int]:
    array_one.sort()
    array_two.sort()
    
    one_ptr = 0
    two_ptr = 0
    
    smallest_diff = None
    smallest_pair = None

    while one_ptr < len(array_one) and two_ptr < len(array_two):
        c1 = array_one[one_ptr]
        c2 = array_two[two_ptr]

        tmp_diff = abs(c2 - c1)

        if tmp_diff == 0:
            return [c1, c2]
        elif smallest_diff is None or tmp_diff < smallest_diff:
            smallest_diff = tmp_diff
            smallest_pair = [c1, c2]

        if c1 < c2:
            one_ptr += 1
        else:
            two_ptr += 1
    
    return smallest_pair
