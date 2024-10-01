from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        smallest = min(nums)
        largest = max(nums)
        small_index = -1
        large_index = -1
        for i in range(len(nums)):
            if small_index == -1 and nums[i] == smallest:
                small_index = i
            if nums[i] == largest:
                large_index = i
        # 0 1 2
        # 0 2 1
        # 0 1 2
        if small_index < large_index:
            return small_index + len(nums) - 1 - large_index
        else:
            return small_index + len(nums) - 2 - large_index