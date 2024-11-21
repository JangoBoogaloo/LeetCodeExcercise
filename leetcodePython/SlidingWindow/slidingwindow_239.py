from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_arr = []
        decrease_index = deque()
        # init first k element
        for i in range(k):
            while decrease_index and nums[i] >= nums[decrease_index[-1]]:
                decrease_index.pop()
            decrease_index.append(i)

        max_arr.append(nums[decrease_index[0]])

        for right in range(k, len(nums)):
            left = right - k
            if decrease_index and decrease_index[0] == left:
                decrease_index.popleft()
            while decrease_index and nums[right] >= nums[decrease_index[-1]]:
                decrease_index.pop()
            decrease_index.append(right)
            max_arr.append(nums[decrease_index[0]])

        return max_arr