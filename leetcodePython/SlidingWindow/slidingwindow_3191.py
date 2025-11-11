from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        operations = 0
        for i in range(2, len(nums)):
            if nums[i-2] == 0:
                operations += 1
                nums[i - 2] = nums[i - 2] ^ 1
                nums[i - 1] = nums[i - 1] ^ 1
                nums[i] = nums[i] ^ 1
        if nums[-1] + nums[-2] != 2:
            return -1
        return operations
