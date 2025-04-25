from typing import List


class Solution:
    def _ship_days(self, weights: List[int], capacity: int) -> int:
        i = 0
        curr_weight = 0
        days_need = 1  # in any situation we need at least 1 day to ship
        while i < len(weights):
            if curr_weight + weights[i] > capacity:
                curr_weight = 0
                days_need += 1
            curr_weight += weights[i]
            i += 1
        return days_need

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left_bound = max(weights)
        right_bound = sum(weights)
        ans = 0
        while left_bound <= right_bound:
            mid = (left_bound + right_bound) // 2
            if self._ship_days(weights, mid) > days:
                left_bound = mid + 1
            else:
                ans = mid
                right_bound = mid - 1
        return ans
