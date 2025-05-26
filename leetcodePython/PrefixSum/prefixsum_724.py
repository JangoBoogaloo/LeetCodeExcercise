from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        currSum = 0
        for i in range(len(nums)):
            rightSum = total - currSum - nums[i]
            if currSum == rightSum:
                return i
            currSum += nums[i]
        return -1





