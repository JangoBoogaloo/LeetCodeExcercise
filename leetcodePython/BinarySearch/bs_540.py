from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            evenMidIndex = (left + right) // 2
            evenMidIndex -= (evenMidIndex % 2)
            if nums[evenMidIndex] == nums[evenMidIndex + 1]:
                left = evenMidIndex + 2
            else:
                right = evenMidIndex
        return nums[left]








