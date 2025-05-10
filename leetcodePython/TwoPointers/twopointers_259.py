from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            count += self.twoSumSmallerCount(nums, i+1, target-nums[i])
        return count

    def twoSumSmallerCount(self, nums: List[int], left: int, target: int) -> int:
        count = 0
        right = len(nums)-1
        while left < right:
            if nums[left] + nums[right] < target:
                # A_i, A_l, [A_l+1, ......A_r]
                count += right-left
                left += 1
            else:
                right -= 1
        return count