from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = odd = 0
        sub_count = ans = 0
        for right, num in enumerate(nums):
            if num % 2 == 1:
                odd += 1
            if odd == k:
                sub_count = 0
            while odd == k:
                if nums[left] % 2 == 1:
                    odd -= 1
                sub_count += 1
                left += 1
            ans += sub_count
        return ans