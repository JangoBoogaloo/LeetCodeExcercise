from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        removals = len(nums) - k
        if removals <= 0:
            return nums
        remainIncreaseDigits = []
        for i in range(len(nums)):
            while remainIncreaseDigits and removals and nums[i] < remainIncreaseDigits[-1]:
                remainIncreaseDigits.pop()
                removals -= 1
            remainIncreaseDigits.append(nums[i])
        if removals:
            remainIncreaseDigits = remainIncreaseDigits[:-removals]
        return remainIncreaseDigits

