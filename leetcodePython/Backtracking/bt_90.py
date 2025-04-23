from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = []
        current: List[int] = []
        nums.sort()

        def backtrack(index: int):
            subsets.append(current[:])
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()

        backtrack(0)
        return subsets
