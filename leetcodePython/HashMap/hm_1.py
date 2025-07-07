from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairIndexMap = {}
        for i in range(len(nums)):
            if nums[i] in pairIndexMap:
                return [i, pairIndexMap[nums[i]]]
            pairIndexMap[target - nums[i]] = i
        return [-1, -1]





