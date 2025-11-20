from typing import List


class Solution:
    def maxNonAdjacentSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] + nums[2]
        leftNonAdjacentMax = float('-inf')
        maxSum = float('-inf')
        for i in range(3, len(nums)):
            leftNonAdjacentMax = max(leftNonAdjacentMax, nums[i-2])
            maxSum = max(maxSum, leftNonAdjacentMax+nums[i])
        return maxSum







import pytest

target = Solution()

@pytest.mark.parametrize("nums, expect",
[
    ([1, 3, 4, 3], 6),
    ([-10, 3, -2], -12),
    ([1, 5, 4, 1, 3], 8),
])
def test_maxNonAdjacentSum(nums, expect):
    assert target.maxNonAdjacentSum(nums) == expect
