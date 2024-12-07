from itertools import accumulate
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefix_sum = list(accumulate(cardPoints))
        window_len = len(cardPoints) - k
        total_points = prefix_sum[-1]
        if window_len <= 0:
            return total_points

        min_remain = prefix_sum[window_len-1]
        for right in range(window_len, len(prefix_sum)):
            curr_remain = prefix_sum[right] - prefix_sum[right-window_len]
            min_remain = min(min_remain, curr_remain)
        return total_points - min_remain
