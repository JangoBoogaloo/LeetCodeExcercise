import bisect
from typing import List


class SolutionBruteForce:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        for query in queries:
            ops = 0
            for num in nums:
                ops += abs(num - query)
            ans.append(ops)
        return ans


class SolutionBS:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        curr_sum = 0
        nums.sort()
        prefix_sum = [0]
        ans = []
        for num in nums:
            curr_sum += num
            prefix_sum.append(curr_sum)
        for query in queries:
            idx = bisect.bisect_left(nums, query)
            ops_for_smaller = query * idx - prefix_sum[idx]
            ops_for_bigger = prefix_sum[-1] - prefix_sum[idx] - query * (len(nums) - idx)
            ans.append(ops_for_smaller + ops_for_bigger)
        return ans
