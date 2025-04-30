from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                three_sum = nums[i] + nums[left] +nums[right]
                diff = target-three_sum
                if abs(diff) < abs(min_diff):
                    # min_diff = target - three_sum
                    # three_sum = target - min_diff
                    min_diff = diff
                if min_diff == 0:
                    break
                if three_sum < target:
                    left += 1
                else:
                    right -= 1
        # min_diff = target - three_sum
        # three_sum = target - min_diff
        return target - min_diff