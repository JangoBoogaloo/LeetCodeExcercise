from typing import List
from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        ans = 0
        subArrayCountOfSum = Counter()
        for num in nums:
            currSum += num
            if currSum == k:
               ans += 1
            diff = currSum - k
            ans += subArrayCountOfSum[diff]
            subArrayCountOfSum[currSum] += 1
        return ans