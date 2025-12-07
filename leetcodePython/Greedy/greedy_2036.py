from typing import List


class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        maxSum = positiveSum = negativeSum = float('-inf')
        for num in nums:
            positiveSum, negativeSum = max(negativeSum + num, num), positiveSum - num
            maxSum = max(maxSum, positiveSum, negativeSum)
        return maxSum