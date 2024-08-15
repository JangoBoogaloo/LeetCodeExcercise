from typing import List


class Solution:
    @staticmethod
    def _getBouquet(bloom_days: List[int], day: int, k: int) ->int:
        adjacent = 0
        bouquet = 0
        for bloom in bloom_days:
            if bloom > day:
                adjacent = 0
            else:
                adjacent += 1
            if adjacent == k:
                bouquet += 1
                adjacent = 0
        return bouquet

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        need_flowers = m * k
        if need_flowers > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            mid_day = (left + right) // 2
            if self._getBouquet(bloomDay, mid_day, k) < m:
                left = mid_day + 1
            else:
                right = mid_day
        return left

