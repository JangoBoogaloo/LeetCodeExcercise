from typing import List
from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = Counter()
        ans = left = 0
        for right, num in enumerate(nums):
            frequency[num] += 1
            while frequency[num] > k:
                frequency[nums[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans

