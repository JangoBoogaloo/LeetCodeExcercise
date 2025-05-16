from typing import List
from heapq import heappush, heappop


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        start_sorted_tasks = [(start, process_time, id) for id, (start, process_time) in enumerate(tasks)]
        start_sorted_tasks.sort()

        curr_time = 0
        visited_task_id = 0
        ready_tasks_time_minheap = []
        ans = []
        while visited_task_id < len(tasks) or ready_tasks_time_minheap:

            # shift current time to next earliest task start time, if we don't have next tasks scheduled
            if not ready_tasks_time_minheap and curr_time < start_sorted_tasks[visited_task_id][0]:
                curr_time = start_sorted_tasks[visited_task_id][0]

            # put all tasks that ready to start in to min heap, using process time to order
            while visited_task_id < len(start_sorted_tasks) and curr_time >= start_sorted_tasks[visited_task_id][0]:
                _, process_time, id = start_sorted_tasks[visited_task_id]
                heappush(ready_tasks_time_minheap, (process_time, id))
                visited_task_id += 1

            process_time, index = heappop(ready_tasks_time_minheap)
            curr_time += process_time
            ans.append(index)
        return ans