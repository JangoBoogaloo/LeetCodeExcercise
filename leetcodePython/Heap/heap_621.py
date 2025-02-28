from typing import List
from collections import Counter, deque
from heapq import *


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        maxCountHeap = [-count for count in task_count.values()]
        heapify(maxCountHeap)
        time = 0
        taskQueue = deque()
        while maxCountHeap or taskQueue:
            time += 1
            if maxCountHeap:
                currentTaskCount = -heappop(maxCountHeap)
                nextTaskCount = currentTaskCount - 1
                if nextTaskCount:
                    nextTaskTime = time + n
                    taskQueue.append((nextTaskCount, nextTaskTime))
            if taskQueue and taskQueue[0][1] == time:
                remainCount, _ = taskQueue.popleft()
                heappush(maxCountHeap, -remainCount)
        return time
