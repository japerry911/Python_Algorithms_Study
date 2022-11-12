from typing import List


def threeNumberSum(array: List[int], target_sum: int) -> List[List[int]]:
    return_list = []
    
    array.sort()

    for c_idx in range(len(array) - 1):
        cn = array[c_idx]
        l_idx = c_idx + 1 
        r_idx = len(array) - 1

        while l_idx < r_idx:
            cs = cn + array[l_idx] + array[r_idx]

            if cs == target_sum:
                return_list.append(
                    [cn, array[l_idx], array[r_idx]]
                )
                l_idx += 1
                r_idx -= 1
            elif cs < target_sum:
                l_idx += 1
            elif cs > target_sum:
                r_idx -= 1

    return return_list
