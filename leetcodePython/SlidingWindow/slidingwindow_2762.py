from typing import List
from collections import deque


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        increase_index_q = deque()
        decrease_index_q = deque()
        ans = left = 0

        for right in range(len(nums)):
            while decrease_index_q and nums[decrease_index_q[-1]] < nums[right]:
                decrease_index_q.pop()
            decrease_index_q.append(right)

            while increase_index_q and nums[increase_index_q[-1]] > nums[right]:
                increase_index_q.pop()
            increase_index_q.append(right)

            while nums[decrease_index_q[0]] - nums[increase_index_q[0]] > 2:
                if decrease_index_q[0] < increase_index_q[0]:
                    left = decrease_index_q[0] + 1
                    decrease_index_q.popleft()
                else:
                    left = increase_index_q[0] + 1
                    increase_index_q.popleft()
            ans += right - left + 1

        return ans
