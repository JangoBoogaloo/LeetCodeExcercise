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
        left, right, total_count = 0, 0, 0
        freq = collections.Counter()
        distinct_count = 0
        duplicate_count = 0
        while right < len(nums):
            new_num = nums[right]
            freq[new_num] += 1

            if freq[new_num] == 1:
                distinct_count += 1

            if distinct_count > k:
                duplicate_count = 0
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct_count -= 1
                left += 1

            if distinct_count == k:
                while freq[nums[left]] > 1:
                    freq[nums[left]] -= 1
                    duplicate_count += 1
                    left += 1
                total_count += (duplicate_count + 1)
            right += 1
        return total_count


