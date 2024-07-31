from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        new_ch_index = 1
        for i in range(1, size):
            if nums[i] != nums[i-1]:
                nums[new_ch_index] = nums[i]
                new_ch_index += 1
        return new_ch_index