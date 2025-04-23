from heapq import heappush, heappop
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], peoples: List[int]) -> List[int]:
        time_people = [(time, p) for p, time in enumerate(peoples)]
        time_people.sort()
        flowers.sort()
        flowerIndex = 0
        minEndTimeHeap = []
        answer = {}
        for time, people in time_people:
            while flowerIndex < len(flowers) and flowers[flowerIndex][0] <= time:
                heappush(minEndTimeHeap, flowers[flowerIndex][1])
                flowerIndex += 1
            while minEndTimeHeap and minEndTimeHeap[0] < time:
                heappop(minEndTimeHeap)
            answer[people] = len(minEndTimeHeap)
        return [answer[i] for i in range(len(peoples))]
