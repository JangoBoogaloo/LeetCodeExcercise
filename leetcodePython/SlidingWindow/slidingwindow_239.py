from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i in range(k):
            # any data before i and smaller than nums[i] is not important anymore, nums[i] is only useful
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        # maximum for the 1st k elements
        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            # out of k range
            if dq and dq[0] == i-k:
                dq.popleft()
            # any data before i and smaller than nums[i] is not important anymore, nums[i] is only useful
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            # dq already resolved, current maximum is in dq top
            res.append(nums[dq[0]])
        return res