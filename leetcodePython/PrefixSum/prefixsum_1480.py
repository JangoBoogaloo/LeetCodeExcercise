from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = [nums[0]]

        for i in range(1, len(nums)):
            sums.append(sums[i - 1] + nums[i])

        return sums

