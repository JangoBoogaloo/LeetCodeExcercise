import collections
from typing import List

class SolutionSubSetApproach:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # With at most K - With at most K-1 = With exactly K
        return self.__subarayWithAtMostKDistinct(nums, k) - self.__subarayWithAtMostKDistinct(nums,k-1)

    def __subarayWithAtMostKDistinct(self, nums: List[int], k: int) -> int:
        left, right, total_count = 0, 0, 0
        num_freq = collections.Counter()
        for right in range(len(nums)):
            num_freq[nums[right]] += 1
            while k < len(num_freq):
                num_freq[nums[left]] -= 1
                if num_freq[nums[left]] == 0:
                    del num_freq[nums[left]]
                left += 1
            window_array_count = right - left + 1
            total_count += window_array_count
        return total_count

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


