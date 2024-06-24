from typing import List
from collections import Counter
from heapq import *


class SolutionMaxHeap:
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


class SolutionSort:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_max_freq = Counter(tasks).most_common()
        print(task_max_freq)
        # it needs 1 less gap than the frequency: 3 characters, 2 gaps
        max_gap = task_max_freq[0][1] - 1
        idle_slots = max_gap * n
        for i in range(1, len(task_max_freq)):
            next_freq = task_max_freq[i][1]
            idle_slots -= min(max_gap, next_freq)

        if idle_slots > 0:
            return idle_slots + len(tasks)
        else:
            return len(tasks)


if __name__ == "__main__":
    sol = SolutionSort()
    sol.leastInterval(["A","A","A","B","B","B"], 2)
