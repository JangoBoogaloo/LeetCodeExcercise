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
            ans = max(ans, right - left + 1)
        return ans


class SolutionMaxWindow:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = Counter()
        ans = left = bad_freq = 0
        for right, num in enumerate(nums):
            frequency[num] += 1
            if frequency[num] == k + 1:
                bad_freq += 1
            if bad_freq:
                frequency[nums[left]] -= 1
                if frequency[nums[left]] == k:
                    bad_freq -= 1
                left += 1
        return len(nums) - left
