from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1):
            if not i % 2 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                continue
            if i % 2 and nums[i] < nums[i+1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]






