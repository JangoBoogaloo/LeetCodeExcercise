import heapq
from typing import List


class SolutionPQ:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        ride_heap = []
        max_last_profit = 0
        for i in range(len(rides)):
            start_i, end_i, tip_i = rides[i]
            if end_i > n:
                continue
            profit_i = end_i - start_i + tip_i
            while ride_heap:
                last_end, last_profit = ride_heap[0]
                if start_i < last_end:
                    break
                max_last_profit = max(max_last_profit, last_profit)
                heapq.heappop(ride_heap)
            rides_with_i = (end_i, max_last_profit + profit_i)
            heapq.heappush(ride_heap, rides_with_i)

        max_profit = 0
        while ride_heap:
            _, chained_profit = heapq.heappop(ride_heap)
            max_profit = max(max_profit, chained_profit)
        return max_profit


class SolutionDP:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        rides.sort()
        for loc in range(n - 1, -1, -1):
            dp[loc] = dp[loc+1]
            while rides:
                start, end, tip = rides[-1]
                if start != loc:
                    break
                profit = (end - start + tip)
                dp[loc] = max(dp[loc], dp[end] + profit)
                rides.pop()
        return dp[0]