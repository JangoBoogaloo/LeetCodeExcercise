from typing import List
from collections import Counter
from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = Counter(tasks)
        max_heap = [-f[1] for f in task_freq.items()]
        heapify(max_heap)
        time = 0
        while max_heap:
            cycle = n + 1
            store = []
            task_count = 0
            while cycle > 0 and max_heap:
                current_freq = -heappop(max_heap)
                if current_freq > 1:
                    store.append(current_freq - 1)
                task_count += 1
                cycle -= 1
            for x in store:
                heappush(max_heap, -x)
            if max_heap:
                time += n + 1
            else:
                time += task_count

        return time