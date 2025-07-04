from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        rightBoundary = len(arr) - 1
        while rightBoundary > 0 and arr[rightBoundary] >= arr[rightBoundary - 1]:
            rightBoundary -= 1
        if rightBoundary == 0:
            return 0
        removeSubarrayLength = rightBoundary
        left = 0
        while left < rightBoundary:
            while rightBoundary < len(arr) and arr[left] > arr[rightBoundary]:
                rightBoundary += 1
            removeSubarrayLength = min(removeSubarrayLength, (rightBoundary - 1) - (left + 1) + 1)
            if arr[left] > arr[left + 1]:
                break
            left += 1
        return removeSubarrayLength







import pytest
target = Solution()

@pytest.mark.parametrize("arr, expect",
[
    ([1, 2], 0), ([1, 1], 0),
    ([2, 1], 1),
    ([1, 2, 1, 1], 1),
    ([1, 2, 3, 2, 2, 1, 1, 1], 4),
    ([1, 2, 3, 2, 2, 1, 2, 3], 4)
])
def test_findLengthOfShortestSubarray(arr, expect):
    assert target.findLengthOfShortestSubarray(arr) == expect