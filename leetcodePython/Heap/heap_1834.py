from typing import List
from heapq import heappush, heappop


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        start_sorted_tasks = [(start, time, id) for id, (start, time) in enumerate(tasks)]
        start_sorted_tasks.sort()

        curr_time = 0
        task_id = 0
        next_tasks = []
        while task_id < len(tasks) or next_tasks:
