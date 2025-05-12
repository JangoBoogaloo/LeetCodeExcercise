from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        left = 0
        ans = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum * (right-left+1) >= k:
                curr_sum -= nums[left]
                left += 1
            ans += right-left + 1
        return ans