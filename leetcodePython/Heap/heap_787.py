from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        start_end_price = defaultdict(list)
        for start, end, price in flights:
            start_end_price[start].append((end, price))

        min_cost_city_stops = [(0, src, 0)]
        stopsToVisit = {}
        while min_cost_city_stops:
            totalCost, currentCity, stops = heappop(min_cost_city_stops)
            if stops > k + 1:
                continue
            if currentCity == dst:
                return totalCost
            if currentCity in stopsToVisit and stopsToVisit[currentCity] == stops:
                continue
            stopsToVisit[currentCity] = stops
            for nextCity, price in start_end_price[currentCity]:
                if nextCity in stopsToVisit and stopsToVisit[nextCity] <= stops:
                    continue
                heappush(min_cost_city_stops, (totalCost+price, nextCity, stops+1))
        return -1
