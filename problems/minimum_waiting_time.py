from typing import List


def minimumWaitingTime(queries: List[int]) -> int:
    queries.sort()

    total_waiting_time = 0
    for idx, duration in enumerate(queries):
        queries_left = len(queries) - (idx + 1)
        total_waiting_time += duration * queries_left

    return total_waiting_time
