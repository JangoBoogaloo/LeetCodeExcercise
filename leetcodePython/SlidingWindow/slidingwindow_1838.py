from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        current_sum = 0
        left = 0
        for right in range(len(nums)):
            freq_num = nums[right]
            current_sum += freq_num
            freq_window_sum = freq_num * (right - left + 1)
            if freq_window_sum - current_sum > k:
                current_sum -= nums[left]
                left += 1
        return len(nums) - left
