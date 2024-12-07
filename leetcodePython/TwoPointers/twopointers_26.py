from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_data_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[new_data_index] = nums[i]
                new_data_index += 1
        return new_data_index
