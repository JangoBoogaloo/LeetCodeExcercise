from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = []
        current: List[int] = []

        def backtrack(index: int):
            subsets.append(current[:])
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()

        backtrack(0)

        return subsets
