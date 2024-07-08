from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        city_used_counts = [0]*n
        for road in roads:
            start_city, end_city = road[0], road[1]
            city_used_counts[start_city] += 1
            city_used_counts[end_city] += 1
        city_used_counts.sort()

        value = 1
        ans = 0
        for count in city_used_counts:
            ans += count*value
            value += 1
        return ans