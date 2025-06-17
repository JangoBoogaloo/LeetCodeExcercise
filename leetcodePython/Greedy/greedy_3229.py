from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        totalOps = 0
        prevOps = 0
        for i in range(len(nums)):
            currentOps = target[i] - nums[i]
            extraOps = max(currentOps - prevOps, 0)
            totalOps += extraOps
            prevOps = currentOps
        return totalOps + max(-prevOps, 0)








import pytest
sol = Solution()

@pytest.mark.parametrize("nums, target, expect",
[
    ([1, 2], [2, 4], 2),
    ([3, 5], [4, 4], 2),
    ([3, 4], [5, 5], 2),
    ([3, 5, 3], [4, 4, 4], 3),
])
def test_minimumOperations(nums, target, expect):
    assert sol.minimumOperations(nums, target) == expect