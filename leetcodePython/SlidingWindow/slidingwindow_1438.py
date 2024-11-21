from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decrease = deque()
        increase = deque()
        left = 0
        for right in range(len(nums)):

            while decrease and nums[right] > decrease[-1]:
                decrease.pop()
            decrease.append(nums[right])

            while increase and nums[right] < increase[-1]:
                increase.pop()
            increase.append(nums[right])

            if decrease[0] - increase[0] > limit:
                if decrease[0] == nums[left]:
                    decrease.popleft()
                if increase[0] == nums[left]:
                    increase.popleft()
                left += 1
        return len(nums) - left
