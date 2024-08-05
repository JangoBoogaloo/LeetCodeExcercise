from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        total_move = 0
        for i  in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                move = nums[i-1] - nums[i] + 1
                nums[i] += move
                total_move += move
        return total_move