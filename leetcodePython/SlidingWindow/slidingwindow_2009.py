from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sortedUnique = sorted(set(nums))
        left = 0
        for right in range(1, len(sortedUnique)):
            if sortedUnique[right] - sortedUnique[left] > len(nums) - 1:
                left += 1
        duplicateCount = len(nums) - len(sortedUnique)
        return left + duplicateCount






import pytest
target = Solution()

@pytest.mark.parametrize("nums, expect",
[
    ([1, 4, 4, 5, 6, 10], 2),
    ([1, 2, 2, 2, 5, 10], 3),
])
def test_minOperations(nums, expect):
    assert target.minOperations(nums) == expect