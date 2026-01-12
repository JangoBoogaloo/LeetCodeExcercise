from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ops = target[0]
        for i in range(1, len(target)):
            ops += max(0, target[i] - target[i-1])
        return ops








import pytest
sol = Solution()

@pytest.mark.parametrize("target, expect",
[
    ([1, 2, 3], 3),
    ([1, 2, 1], 2),
    ([3, 1, 2], 4),
    ([1, 3, 2, 1], 3),
])
def test_minNumberOperations(target, expect):
    assert sol.minNumberOperations(target) == expect