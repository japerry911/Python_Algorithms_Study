from typing import List


# O(n) time | O(1) space
def isValidSubsequence(array: List, sequence: List) -> bool:
    seq_idx = 0
    array_idx = 0

    while seq_idx < len(sequence) and array_idx < len(array):
        if sequence[seq_idx] == array[array_idx]:
            seq_idx += 1

        array_idx += 1

    return seq_idx == len(sequence)