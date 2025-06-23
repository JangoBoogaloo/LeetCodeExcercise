from typing import List


class Solution:
    _REPEAT_LIMIT = 2

    def removeDuplicates(self, nums: List[int]) -> int:
        new_data_index = 0
        repeat = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[new_data_index] = nums[i]
                new_data_index += 1
                repeat = 1
            elif repeat < self._REPEAT_LIMIT:
                repeat += 1
                nums[new_data_index] = nums[i]
                new_data_index += 1
        return new_data_index
