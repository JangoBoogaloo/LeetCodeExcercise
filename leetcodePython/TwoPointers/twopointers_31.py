from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        non_ascending_index = len(nums) - 1
        while non_ascending_index > 0 and nums[non_ascending_index-1] >= nums[non_ascending_index]:
            non_ascending_index -= 1

        if non_ascending_index == 0:
            nums.reverse()
            return

        greater_index = len(nums)-1
        while nums[greater_index] <= nums[non_ascending_index-1]:
            greater_index -= 1

        # swap
        nums[non_ascending_index-1], nums[greater_index] = nums[greater_index], nums[non_ascending_index-1]
        # reverse
        nums[non_ascending_index:]= nums[len(nums)-1:non_ascending_index-1:-1]
