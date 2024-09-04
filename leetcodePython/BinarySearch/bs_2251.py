import collections
import heapq
from typing import List


class SolutionSweepLinePrefixSumBruteForce:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        time_slots = max([x[1] for x in flowers])
        print(time_slots)
        flower_change = [0] * (time_slots + 2)
        flower_change[-1] = 0
        for start, end in flowers:
            flower_change[start] += 1
            flower_change[end + 1] -= 1
        flowers_at_time = []
        curr_flowers = 0
        for time in range(len(flower_change)):
            curr_flowers += flower_change[time]
            flowers_at_time.append(curr_flowers)

        ans = []
        for arrive_time in people:
            if arrive_time > time_slots:
                ans.append(0)
            else:
                ans.append(flowers_at_time[arrive_time])
        return ans


class SolutionHeap:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # n*log(n)
        flowers.sort()
        # m*log(m)
        sorted_people = sorted(people)
        heap_end_time = []
        time_i = 0
        ans = {}
        # O(m)
        for arrive_time in sorted_people:
            while time_i < len(flowers):
                start, end = flowers[time_i]
                if start > arrive_time:
                    break
                # log(n)
                heapq.heappush(heap_end_time, end)
                time_i += 1
            while heap_end_time and heap_end_time[0] < arrive_time:
                heapq.heappop(heap_end_time)
            ans[arrive_time] = len(heap_end_time)

        return [ans[time] for time in people]


