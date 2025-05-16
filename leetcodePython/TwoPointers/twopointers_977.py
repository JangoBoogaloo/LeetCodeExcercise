from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        result = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                bigger = nums[right]
                right -= 1
            else:
                bigger = nums[left]
                left += 1
            result[i] = bigger*bigger
        return result




import pytest
target = Solution()

@pytest.mark.parametrize("nums, expect",
[
    ([-4, -2, 0, 1, 3], [0, 1, 4, 9, 16]),
    ([-5, -3, -2, -1], [1, 4, 9, 25]),
])
def test_sortedSquares(nums, expect):
    assert target.sortedSquares(nums) == expect