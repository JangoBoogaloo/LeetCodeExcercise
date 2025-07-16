from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectSum = len(nums) * (len(nums) + 1) // 2
        actualSum = sum(nums)
        return expectSum - actualSum






