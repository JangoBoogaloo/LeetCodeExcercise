import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_info = collections.defaultdict(dict)
        for start, end, price in flights:
            flight_info[start][end] = price

        heap = [(0, src, k + 1)]

        while heap:
            price, start, k = heapq.heappop(heap)
            if start == dst:
                return price
            if k > 0:
                for end in flight_info[start].keys():
                    heapq.heappush(heap, (price + flight_info[start][end], end, k-1))
        return -1

