from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0
        left = 0

        for right in range(len(nums)):
            if not nums[right]:
                zero_count += 1
            if zero_count > k:
                if not nums[left]:
                    zero_count -= 1
                left += 1
        return len(nums) - left
