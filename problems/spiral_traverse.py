from typing import List


def spiralTraverse(array: List[int]) -> List[List[int]]:
    if len(array) == 1:
        return array[0]
    
    spiral = []

    row_start = 0
    row_end = len(array) - 1
    column_start = 0
    column_end = len(array[0]) - 1

    while row_start <= row_end and column_start <= column_end: 
        for i in range(column_start, column_end + 1):
            spiral.append(array[row_start][i])

        for i in range(row_start + 1, row_end + 1):
            spiral.append(array[i][column_end])
                
        for i in reversed(range(column_start, column_end)):
            if row_start == row_end:
                break

            spiral.append(array[row_end][i])

        for i in reversed(range(row_start + 1, row_end)):
            if column_start == column_end:
                break

            spiral.append(array[i][column_start])

        column_start += 1
        row_start += 1
        column_end -= 1
        row_end -= 1

    return spiral
