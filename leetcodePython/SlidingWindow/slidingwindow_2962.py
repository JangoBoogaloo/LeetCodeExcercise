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