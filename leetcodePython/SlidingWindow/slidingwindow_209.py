from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        min_len = float("inf")
        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target and left <= right:
                min_len = min(min_len, right-left+1)
                curr_sum -= nums[left]
                left += 1
        if min_len == float("inf"):
            return 0
        return min_len