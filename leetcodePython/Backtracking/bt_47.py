from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations: List[List[int]] = []
        current: List[int] = []
        nums.sort()
        used: List[bool] = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                permutations.append(current[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # not used[i-1]: this duplicate number is not being considered in permutation
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                current.append(nums[i])
                backtrack()
                used[i] = False
                current.pop()

        backtrack()
        return permutations
