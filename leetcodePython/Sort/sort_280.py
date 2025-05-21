from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1):
            if i % 2 == 0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                continue
            if i % 2 == 1 and nums[i] < nums[i+1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


class SolutionSort:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        for i in range(1, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]





