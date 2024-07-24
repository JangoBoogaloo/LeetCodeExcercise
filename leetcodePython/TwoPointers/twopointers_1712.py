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


class SolutionTwoPointers:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
        '''
        prefix[left_end] <= prefix[mid_end] - prefix[left_end] <= prefix[right_end] - prefix[mid_end]
        ->
        2*prefix[left_end] <= prefix[mid_end]
        2*prefix[mid_end] <= prefix[left_end] + prefix[-1]
        '''
        mid_min = 0
        mid_max = 0
        ans = 0
        # [0, 0, 0, 0]
        #     l  m
        for left_end in range(1, len(prefix_sum)):
            mid_min = max(mid_min, left_end+1)

            # 2 * prefix[left_end] <= prefix[mid_end]
            while mid_min < len(nums) and prefix_sum[mid_min] < 2 * prefix_sum[left_end]:
                mid_min += 1
            mid_max = max(mid_max, mid_min)
            max_bound = prefix_sum[left_end] + prefix_sum[-1]
            while mid_max < len(nums) and 2 * prefix_sum[mid_max] <= max_bound:
                mid_max += 1
            ans += mid_max - mid_min
        return ans % 1_000_000_007
