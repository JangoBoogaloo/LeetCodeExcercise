from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        oddCount, evenCount, alternateCount = 0, 0, 1
        prevDivisibleByTwo = nums[0] % 2
        for num in nums:
            divisibleByTwo = num % 2
            if divisibleByTwo:
                evenCount += 1
            else:
                oddCount += 1
            if prevDivisibleByTwo != divisibleByTwo:
                alternateCount += 1
            prevDivisibleByTwo = divisibleByTwo
        return max(oddCount, evenCount, alternateCount)






import pytest
target = Solution()

@pytest.mark.parametrize("nums, expect",
[
    ([2, 4, 6], 3),
    ([2, 3, 4, 6, 8], 4),
    ([1, 3, 5], 3),
    ([1, 2, 3, 5, 7], 4),
    ([1, 2, 3, 4], 4)
])
def test_maximumLength(nums, expect):
    assert target.maximumLength(nums) == expect