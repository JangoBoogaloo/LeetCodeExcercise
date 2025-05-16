from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = zero_count = 0
        for right, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            if zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

        return right - left