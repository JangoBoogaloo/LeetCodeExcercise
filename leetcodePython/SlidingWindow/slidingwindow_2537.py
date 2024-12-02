import collections
from typing import List
from collections import Counter


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = left = 0
        count = Counter()
        new_pairs = 0
        for right in range(len(nums)):
            new_pairs += count[nums[right]]
            count[nums[right]] += 1
            while new_pairs >= k:
                count[nums[left]] -= 1
                new_pairs -= count[nums[left]]
                left += 1
            ans += left
        return ans
