from itertools import accumulate
from typing import List
from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums.sort()
        prefixSum = [0] + list(accumulate(nums))

        for query in queries:
            idx = bisect_left(nums, query)
            queryIndexSum = query * idx
            smallerOps = queryIndexSum - prefixSum[idx]
            biggerOps = prefixSum[-1] - prefixSum[idx] - query * (len(nums) - idx)
            answer.append(smallerOps + biggerOps)
        return answer










import pytest
target = Solution()

@pytest.mark.parametrize("nums, queries, expect",
[
    ([1, 2], [1], [1]),
    ([1, 2], [2], [1]),
    ([1, 2, 3], [2], [2]),
])
def test_minOperations(nums, queries, expect):
    assert target.minOperations(nums, queries) == expect