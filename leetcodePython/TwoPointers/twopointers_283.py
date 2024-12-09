from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZeroIndex = 0
        for num in nums:
            if num != 0:
                nums[nonZeroIndex] = num
                nonZeroIndex += 1
        for i in range(nonZeroIndex, len(nums)):
            nums[i] = 0
