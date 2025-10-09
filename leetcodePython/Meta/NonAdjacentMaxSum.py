from typing import List


class Solution:
    def maxNonAdjacentSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] + nums[2]
        leftNonAdjacentMax = float('-inf')
        maxSum = float('-inf')
        for i in range(3, len(nums)):
            leftNonAdjacentMax = max(leftNonAdjacentMax, nums[i-2])
            maxSum = max(maxSum, leftNonAdjacentMax+nums[i])
        return maxSum







