from typing import List


def findThreeLargestNumbers(array: List[int]) -> List[int]:
    three_largest = [array.pop(0)]
    three_largest.append(array.pop(0))
    three_largest.append(array.pop(0))
    three_largest.sort()

    for x in array:
        if x > three_largest[0]:
            if x > three_largest[1]:
                if x > three_largest[2]:
                    three_largest.append(x)
                else:
                    three_largest.insert(2, x)
            else: 
                three_largest.insert(1, x)
        else:
            continue

        three_largest.pop(0)

    return three_largest
