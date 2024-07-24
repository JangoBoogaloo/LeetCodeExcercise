import bisect
from typing import List


class SolutionBinarySearch:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix_sum = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            prefix_sum.append(curr_sum)
        '''
        prefix[left_end] <= prefix[mid_end] - prefix[left_end] <= prefix[right_end] - prefix[mid_end]
        ->
        2*prefix[left_end] <= prefix[mid_end]
        2*prefix[mid_end] <= prefix[left_end] + prefix[-1]
        '''
        ans = 0
        for left_end in range(0, len(prefix_sum)-2):
            mid_end_min = bisect.bisect_left(prefix_sum, prefix_sum[left_end]*2)
            mid_end_max = bisect.bisect_right(prefix_sum, (prefix_sum[left_end] + prefix_sum[-1]) // 2)
            mid_end_min = max(mid_end_min, left_end+1)
            mid_end_max = min(mid_end_max, len(prefix_sum)-1)
            ans += max(0, mid_end_max - mid_end_min)
        return ans % 1_000_000_007