from typing import List
from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_q = deque()
        max_q = deque()
        ans = left = 0
        for right in range(len(nums)):
            while max_q and nums[max_q[-1]] < nums[right]:
                max_q.pop()
            max_q.append(right)

            while min_q and nums[min_q[-1]] > nums[right]:
                min_q.pop()
            min_q.append(right)

            while nums[max_q[0]] - nums[min_q[0]] > 2:
                if max_q[0] < min_q[0]:
                    left = max_q[0] + 1
                    max_q.popleft()
                else:
                    left = min_q[0] + 1
                    min_q.popleft()
            ans += right - left + 1

        return ans
