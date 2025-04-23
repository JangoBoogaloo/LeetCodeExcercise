from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def _at_most(nums: List[int], max_num: int) -> int:
        count = Counter()
        left = 0
        ans = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            while len(count) > max_num:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            ans += right - left + 1
        return ans

    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        num_count = len(nums)
        total_sub_arrays = num_count * (num_count + 1) // 2
        unique_nums = set(nums)
        left, right = 1, len(unique_nums)
        while left < right:
            guess = (left + right) // 2
            if self._at_most(nums, guess) * 2 < total_sub_arrays:
                left = guess + 1
            else:
                right = guess
        return left