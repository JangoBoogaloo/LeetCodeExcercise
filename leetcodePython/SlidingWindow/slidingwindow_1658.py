from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        remain = total - x
        left = 0
        num_sum = 0
        size = len(nums)
        max_remain = -1
        for right in range(size):
            num_sum += nums[right]
            while num_sum > remain and left <= right:
                num_sum -= nums[left]
                left += 1
            if num_sum == remain:
                max_remain = max(max_remain, right - left + 1)
        if max_remain == -1:
            return -1
        return size - max_remain