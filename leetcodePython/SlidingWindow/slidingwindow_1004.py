from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        freq = left = right = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                freq += 1
            replace = right - left + 1 - freq
            if replace > k:
                if nums[left] == 1:
                    freq -= 1
                left += 1
        return right - left + 1
