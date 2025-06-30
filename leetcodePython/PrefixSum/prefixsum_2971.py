from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        nums.sort()
        prevSum = nums[0] + nums[1]
        perimeter = -1
        for i in range(2, len(nums)):
            currSum = prevSum + nums[i]
            if nums[i] < prevSum:
                perimeter = currSum
            prevSum = currSum
        return perimeter





