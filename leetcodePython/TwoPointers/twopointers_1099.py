from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        maxSum = -1
        while left < right:
            currSum = nums[left] + nums[right]
            if currSum < k:
                maxSum = max(maxSum, currSum)
                left += 1
            else:
                right -= 1
        return maxSum
