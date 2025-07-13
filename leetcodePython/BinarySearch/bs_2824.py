from typing import List
from bisect import  bisect_left


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        pairs = 0
        left, right = 0, len(nums) - 1
        while left < right:
            remain = target - nums[left]
            right = bisect_left(nums, remain) - 1
            pairs += max(0, right - left)
            left += 1
        return pairs





