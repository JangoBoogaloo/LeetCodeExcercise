from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        current = []
        permutations = []
        using = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                a_case = current.copy()
                permutations.append(a_case)
                return
            for i in range(len(nums)):
                if using[i]:
                    continue
                current.append(nums[i])
                using[i] = True
                backtrack()
                current.pop()
                using[i] = False

        backtrack()
        return permutations
