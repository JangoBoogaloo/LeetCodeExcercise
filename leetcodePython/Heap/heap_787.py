from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        start_end_price = defaultdict(list)
        for start, end, price in flights:
            start_end_price[start].append((end, price))

        min_cost_city_stops = [(0, src, 0)]
        visited = {}
        while min_cost_city_stops:
            totalCost, current, stops = heappop(min_cost_city_stops)
            if stops > k + 1:
                continue
            if current == dst:
                return totalCost
            if current in visited and visited[current] == stops:
                continue
            visited[current] = stops
            for end, price in start_end_price[current]:
                if end not in visited or visited[end] > stops:
                    heappush(min_cost_city_stops, (totalCost+price, end, stops+1))
        return -1
