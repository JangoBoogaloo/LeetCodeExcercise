from typing import List
from heapq import heappush, heappop


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        start_duration_id = [(start, duration, task_id) for task_id, (start, duration) in enumerate(tasks)]
        start_duration_id.sort()
        scheduledDurationQ = []
        currentTime = 0

        i = 0
        execution_order = []
        while i < len(tasks) or scheduledDurationQ:
            if not scheduledDurationQ:
                currentTime = max(currentTime, start_duration_id[i][0])

            while i < len(tasks) and currentTime >= start_duration_id[i][0]:
                _, duration, task_id = start_duration_id[i]
                heappush(scheduledDurationQ, (duration, task_id))
                i += 1

            duration, task_id = heappop(scheduledDurationQ)
            currentTime += duration
            execution_order.append(task_id)
        return execution_order
