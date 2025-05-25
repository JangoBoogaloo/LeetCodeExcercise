from typing import List
from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        decrease_sum_index_within_k = deque()
        dp_max_sum_for_index = [0] * len(nums)

        for right in range(len(nums)):
            if decrease_sum_index_within_k and decrease_sum_index_within_k[0] < right - k:
                decrease_sum_index_within_k.popleft()

            if decrease_sum_index_within_k:
                max_sum_index = decrease_sum_index_within_k[0]
                dp_max_sum_for_index[right] = dp_max_sum_for_index[max_sum_index] + nums[right]
            else:
                dp_max_sum_for_index[right] = nums[right]

            while decrease_sum_index_within_k and dp_max_sum_for_index[decrease_sum_index_within_k[-1]] < dp_max_sum_for_index[right]:
                decrease_sum_index_within_k.pop()

            if dp_max_sum_for_index[right] > 0:
                decrease_sum_index_within_k.append(right)
        return max(dp_max_sum_for_index)
