from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_ramp = 0
        decrease_stack = []

        # retrieve the decreasing pattern from nums
        for i, num in enumerate(nums):
            if not decrease_stack or nums[decrease_stack[-1]] > num:
                decrease_stack.append(i)

        # base on decreasing pattern, go from end of nums, try to find the max width, such that:
        # the data from decreasing pattern is smaller than current number
        for i in range(len(nums))[::-1]:
            while decrease_stack and nums[decrease_stack[-1]] <= nums[i]:
                last_index = decrease_stack.pop()
                max_ramp = max(max_ramp, i - last_index)

        return max_ramp