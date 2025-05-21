from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        increaseNumStack = []
        valid = len(nums)
        for i in range(len(nums)):
            while increaseNumStack and nums[i] < increaseNumStack[-1]:
                increaseNumStack.pop()
            valid += len(increaseNumStack)
            increaseNumStack.append(nums[i])
        return valid
