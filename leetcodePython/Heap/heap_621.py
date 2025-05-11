from typing import List
from collections import Counter, deque
from heapq import *


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        maxCountHeap = [-count for count in task_count.values()]
        heapify(maxCountHeap)
        time = 0
        count_time_queue = deque()
        while maxCountHeap or count_time_queue:
            time += 1
            if maxCountHeap:
                currentTaskCount = -heappop(maxCountHeap)
                nextTaskCount = currentTaskCount - 1
                if nextTaskCount:
                    nextTaskTime = time + n
                    count_time_queue.append((nextTaskCount, nextTaskTime))
            if count_time_queue and count_time_queue[0][1] == time:
                remainCount, _ = count_time_queue.popleft()
                heappush(maxCountHeap, -remainCount)
        return time
