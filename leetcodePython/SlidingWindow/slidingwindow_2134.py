from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        windowSize = sum(nums)
        if windowSize < 2:
            return 0
        minSwap = len(nums)
        left = 0
        zeroCount = 0
        for right in range(len(nums) * 2):
            if nums[right % len(nums)] == 0:
                zeroCount += 1
            if right - left + 1 == windowSize:
                minSwap = min(minSwap, zeroCount)
                if nums[left % len(nums)] == 0:
                    zeroCount -= 1
                left += 1
        return minSwap





import pytest
target = Solution()

@pytest.mark.parametrize("nums, expect",
[
    ([1, 0, 1, 0], 1),
    ([1, 0, 1, 1], 0),
    ([1, 0], 0),
    ([0, 0, 0], 0),
])
def test_minSwaps(nums, expect):
    assert target.minSwaps(nums) == expect