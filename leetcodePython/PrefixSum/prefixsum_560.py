from typing import List
from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumul_sum = 0
        ans = 0
        cumul_sum_count = Counter()
        for num in nums:
            cumul_sum += num
            if cumul_sum == k:
               ans += 1
            diff = cumul_sum - k

            # k = curr_sum - diff
            # the count here shows how many cumulate sub array we can subtract to form a valid sub array
            ans += cumul_sum_count[diff]
            cumul_sum_count[cumul_sum] += 1
        return ans