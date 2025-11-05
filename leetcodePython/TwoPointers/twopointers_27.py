from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        non_val_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[non_val_index] = nums[i]
                non_val_index += 1
        return non_val_index
