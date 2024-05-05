from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # if len(nums) < 3: return -1
        nums.sort()
        prev_sum = 0
        ans = -1
        for num in nums:
            if num < prev_sum:
                ans = num + prev_sum
            prev_sum += num
        return ans
