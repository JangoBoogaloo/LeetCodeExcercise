from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        total = 0
        min_i = max_i = out_left = -1
        for right in range(len(nums)):
            if nums[right] > maxK or nums[right] < minK:
                out_left = right
                continue
            if nums[right] == minK:
                min_i = right
            if nums[right] == maxK:
                max_i = right
            in_left = min(min_i, max_i)
            total += max(0, in_left - out_left)
        return total
