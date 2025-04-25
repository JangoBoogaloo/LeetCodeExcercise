from typing import List


class SolutionConcatArray:
    def minSwaps(self, nums: List[int]) -> int:
        # window_size = total_ones = sum(nums)
        window_size = sum(nums)
        if window_size < 2:
            return 0
        circular_nums = nums + nums
        zeros_in_window = 0
        min_swap = len(nums)
        left = 0
        for right, right_num in enumerate(circular_nums):
            if right_num == 0:
                zeros_in_window += 1
            if right - left + 1 == window_size:
                min_swap = min(min_swap, zeros_in_window)
                if circular_nums[left] == 0:
                    zeros_in_window -= 1
                left += 1
        return min_swap


class SolutionInplace:
    def minSwaps(self, nums: List[int]) -> int:
        # window_size = total_ones = sum(nums)
        window_size = sum(nums)
        if window_size < 2:
            return 0
        zeros_in_window = 0
        min_swap = len(nums)
        l = 0
        for r in range(len(nums) * 2):
            if nums[r % len(nums)] == 0:
                zeros_in_window += 1
            if r - l + 1 == window_size:
                min_swap = min(min_swap, zeros_in_window)
                if nums[l % len(nums)] == 0:
                    zeros_in_window -= 1
                l += 1
        return min_swap
