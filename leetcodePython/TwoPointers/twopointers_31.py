from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        rightDecreasingIndex = len(nums) - 1
        while rightDecreasingIndex > 0 and nums[rightDecreasingIndex-1] >= nums[rightDecreasingIndex]:
            rightDecreasingIndex -= 1
        if rightDecreasingIndex == 0:
            nums.reverse()
            return
        smallerIndex = rightDecreasingIndex - 1
        greaterIndex = len(nums) - 1
        while nums[greaterIndex] <= nums[smallerIndex]:
            greaterIndex -= 1

        nums[smallerIndex], nums[greaterIndex] = nums[greaterIndex], nums[smallerIndex]
        nums[rightDecreasingIndex:] = nums[len(nums)-1:rightDecreasingIndex-1:-1]
