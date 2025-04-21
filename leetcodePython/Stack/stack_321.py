from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        return []




import pytest
target = Solution()

@pytest.mark.parametrize("nums1, nums2, k, expect",
[
    ([], [], -1, []),
])
def test_checkType(nums1, nums2, k, expect):
    assert target.maxNumber(nums1, nums2, k) == expect