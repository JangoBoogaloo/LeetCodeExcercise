from itertools import accumulate
from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        index_request_count = [0]*(len(nums)+1)
        for start, end in requests:
            index_request_count[start] += 1
            index_request_count[end+1] -= 1
        index_request_count = list(accumulate(index_request_count[:-1]))
        sorted_nums = sorted(nums)
        index_request_count.sort()
        res = 0
        for i in range(len(sorted_nums)):
            res += index_request_count[i]*sorted_nums[i]
        return res % (10**9 + 7)
