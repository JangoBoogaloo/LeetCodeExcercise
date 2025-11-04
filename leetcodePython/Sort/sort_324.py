from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        smallerHalf = len(nums[::2])
        nums[::2], nums[1::2] = nums[:smallerHalf][::-1], nums[smallerHalf:][::-1]





