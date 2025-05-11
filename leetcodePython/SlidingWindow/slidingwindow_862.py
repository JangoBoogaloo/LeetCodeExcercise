from typing import List
from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        sums = [0]
        for x in nums:
            sums.append(sums[-1] + x)
        monosum_index_q = deque()
        ans = len(nums) + 1
        for right, sum in enumerate(sums):
            # maintain the index such
            while monosum_index_q and sums[monosum_index_q[-1]] >= sum:
                monosum_index_q.pop()
            while monosum_index_q:
                left = monosum_index_q[0]
                if sum - sums[left] < k:
                    break
                ans = min(ans, right - left)
                monosum_index_q.popleft()
            monosum_index_q.append(right)

        if ans < len(nums) + 1:
            return ans
        return -1
