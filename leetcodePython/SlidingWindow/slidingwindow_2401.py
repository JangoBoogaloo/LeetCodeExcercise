from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        sum_AND = 0
        max_window = 0
        left = 0
        for right in range(len(nums)):
            while sum_AND & nums[right] != 0:
                sum_AND = sum_AND ^ nums[left]
                left += 1
            sum_AND = sum_AND | nums[right]
            max_window = max(max_window, right-left+1)
        return max_window
