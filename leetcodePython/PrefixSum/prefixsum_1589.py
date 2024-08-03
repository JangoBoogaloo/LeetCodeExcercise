from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        index_request_count = [0] * (len(nums) + 1)
        for start, end in requests:
            index_request_count[start] += 1
            index_request_count[end + 1] -= 1
        index_request_count = index_request_count[:-1]
        for i in range(1, len(nums)):
            index_request_count[i] += index_request_count[i - 1]
        sorted_nums = sorted(nums)
        sorted_index = sorted(index_request_count)
        res = 0
        for i in range(len(nums)):
            res += sorted_index[i] * sorted_nums[i]
        return res % (10 ** 9 + 7)
