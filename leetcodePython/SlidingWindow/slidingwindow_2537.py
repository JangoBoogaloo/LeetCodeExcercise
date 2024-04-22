import collections
from typing import List
from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = left = 0
        count = Counter()
        for right, num in enumerate(nums):
            k -= count[num]
            count[num] += 1
            while k <= 0:
                count[nums[left]] -= 1
                k += count[nums[left]]
                left += 1
            ans += left
        return ans
