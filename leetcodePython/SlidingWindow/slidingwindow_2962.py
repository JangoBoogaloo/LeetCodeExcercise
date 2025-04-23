from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        ans = left = num_count = 0
        for right in range(len(nums)):
            if nums[right] == max_num:
                num_count += 1
            while num_count == k:
                if nums[left] == max_num:
                    num_count -= 1
                left += 1
            ans += left
        return ans


class SolutionEasyUnderstand:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        max_freq = 0
        left = 0
        total = 0
        current_sub = 0
        for right in range(len(nums)):
            if nums[right] == maximum:
                max_freq += 1
            while max_freq >= k:
                current_sub += 1
                if nums[left] == maximum:
                    max_freq -= 1
                left += 1
            total += current_sub
        return total
