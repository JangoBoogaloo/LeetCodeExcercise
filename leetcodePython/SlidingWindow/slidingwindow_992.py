import collections
from typing import List


class SolutionSubSetApproach:
    def _subarrayWithAtMostX(self, nums: List[int], x: int) -> int:
        left, total, diff = 0, 0, 0
        freq = collections.Counter()
        for right in range(len(nums)):
            freq[nums[right]] += 1
            if freq[nums[right]] == 1:
                diff += 1
            while diff > x:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    diff -= 1
                left += 1
            total += right - left + 1
        return total

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self._subarrayWithAtMostX(nums, k) - self._subarrayWithAtMostX(nums, k-1)


class SolutionSlidingWindow:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        freq = collections.Counter()
        left = 0
        sub_arrays = 0
        total = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1
            if freq[nums[right]] == 1:
                k -= 1
            if k < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    k += 1
                left += 1
                sub_arrays = 0
            if k == 0:
                while freq[nums[left]] > 1:
                    freq[nums[left]] -= 1
                    left += 1
                    sub_arrays += 1
                total += sub_arrays + 1
        return total
